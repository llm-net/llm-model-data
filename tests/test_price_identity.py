"""Price references cannot become implicit routing or cross-product price fallback."""
from copy import deepcopy
import json
import unittest

from test_catalog import c, ROOT


class PriceIdentity(unittest.TestCase):
    def setUp(self):
        self.api = c.read_json(ROOT / "providers/ark/offerings/api-cn/catalog.json")
        self.plan = c.read_json(ROOT / "providers/ark/offerings/agent-plan-cn/catalog.json")
        self.docs = [self.api, self.plan]
        self.short = c.lookup_model(self.docs, "ark", "api-cn", "doubao-seedance-2-0-mini")
        self.dated = c.lookup_model(self.docs, "ark", "api-cn", "doubao-seedance-2-0-mini-260615")

    def test_short_and_dated_preserve_separate_identity(self):
        self.assertIsNone(self.short["request_id"])
        self.assertIsNone(self.short["alias_of"])
        self.assertEqual(self.dated["request_id"], "doubao-seedance-2-0-mini-260615")
        self.assertEqual(self.short["reference_prices"]["rules"][0]["rates"],
                         self.dated["usage_prices"]["rules"][0]["rates"])
        c.check_reference_targets(self.docs)

    def test_product_scoped_local_and_request_names(self):
        short = c.lookup_model(self.docs, "ark", "agent-plan-cn", "doubao-seedance-2-0-mini")
        dotted = c.lookup_model(self.docs, "ark", "agent-plan-cn", "doubao-seedance-2.0-mini")
        self.assertIs(short, dotted)
        self.assertIsNot(short, self.short)
        for provider, offering, name in [("other", "api-cn", self.short["id"]),
                                         ("ark", "api-cn", "DOUBAO-SEEDANCE-2-0-MINI"),
                                         ("ark", "api-cn", "doubao-seedance-2-0-mini-260616")]:
            with self.subTest(name=name), self.assertRaises(c.CatalogError):
                c.lookup_model(self.docs, provider, offering, name)

    def test_ambiguous_local_and_request_names_rejected(self):
        self.short["request_id"] = self.dated["id"]
        with self.assertRaises(c.CatalogError):
            c.lookup_model(self.docs, "ark", "api-cn", self.dated["id"])
        # Collision with a local ID even when the other row has no request ID.
        self.dated["request_id"] = None
        with self.assertRaisesRegex(c.CatalogError, "ambiguous model lookup"):
            c.check_offering(ROOT, self.api, c.read_json(ROOT / "providers/ark/provider.json"))

    def test_latest_revision_uses_dates_and_exact_family(self):
        models = [{"id": x} for x in ["video-261201", "video-260101", "video-mini-270101", "video-260901"]]
        self.assertEqual(c.latest_dated_model(models, "video")["id"], "video-261201")
        self.assertEqual(c.latest_dated_model(list(reversed(models)), "video")["id"], "video-261201")
        with self.assertRaisesRegex(c.CatalogError, "invalid model revision date"):
            c.latest_dated_model(models + [{"id": "video-260231"}], "video")

    def test_new_revision_requires_explicit_reference_update(self):
        newer = deepcopy(self.dated)
        newer["id"] = newer["request_id"] = "doubao-seedance-2-0-mini-260901"
        self.api["models"].append(newer)
        with self.assertRaisesRegex(c.CatalogError, "not latest dated"):
            c.check_reference_targets(self.docs)

    def test_wrong_series_is_not_compatible(self):
        origin = self.short["reference_prices"]["rules"][0]["reference_origin"]
        origin["subject"] = origin["catalog_model"]["model_id"] = "doubao-seedance-2-0-260128"
        with self.assertRaisesRegex(c.CatalogError, "not latest dated"):
            c.check_reference_targets(self.docs)

    def test_price_and_quantity_drift_rejected(self):
        rule = self.short["reference_prices"]["rules"][0]
        for field, value in [("amount", "9.2"), ("per", 1), ("unit", "second"),
                             ("quantity", {**rule["rates"][0]["quantity"], "fields": ["$.usage.total_tokens"]})]:
            original = deepcopy(rule["rates"][0])
            with self.subTest(field=field):
                rule["rates"][0][field] = value
                with self.assertRaisesRegex(c.CatalogError, "rates drift"):
                    c.check_reference_targets(self.docs)
            rule["rates"][0] = original

    def test_cross_provider_and_missing_reference_rejected(self):
        origin = self.short["reference_prices"]["rules"][0]["reference_origin"]
        origin["catalog_model"]["provider_id"] = "other"
        with self.assertRaisesRegex(c.CatalogError, "offering missing"):
            c.check_reference_targets(self.docs)
        other = deepcopy(self.api)
        other["provider_id"] = "other"
        other["models"] = [deepcopy(self.dated)]
        with self.assertRaisesRegex(c.CatalogError, "cross providers"):
            c.check_reference_targets(self.docs + [other])

    def test_reference_cannot_chain_or_inherit_unknown(self):
        self.dated["usage_prices"]["status"] = "unknown"
        self.dated["usage_prices"]["rules"] = []
        with self.assertRaisesRegex(c.CatalogError, "verified usage prices"):
            c.check_reference_targets(self.docs)

    def test_legacy_url_reference_remains_valid(self):
        for doc in self.docs:
            for m in doc["models"]:
                for r in m["reference_prices"]["rules"]:
                    r["reference_origin"].pop("catalog_model", None)
        c.check_reference_targets(self.docs)
        schema = c.Draft202012Validator(c.read_json(ROOT / "schemas/catalog.schema.json"))
        self.assertTrue(schema.is_valid(self.api))

    def test_review_includes_structured_price_source(self):
        old = deepcopy(self.api)
        for m in old["models"]:
            for r in m["reference_prices"]["rules"]:
                r["reference_origin"].pop("catalog_model", None)
        key = "providers/ark/offerings/api-cn/catalog.json"
        report = c.summarize_changes({key: json.dumps(old).encode()}, {key: json.dumps(self.api).encode()})
        self.assertIn('"selection": "latest_dated"', report)
        self.assertIn('"model_id": "doubao-seedance-2-0-mini-260615"', report)

    def test_fable_api_and_subscription_baselines(self):
        docs = [c.read_json(ROOT / f"providers/anthropic/offerings/{offering}/catalog.json")
                for offering in ("api-global", "claude-code")]
        c.check_reference_targets(docs)
        for model_id, cache in [("claude-fable-5-1", "0.25"), ("claude-fable-5", "1")]:
            model = c.lookup_model(docs, "anthropic", "api-global", model_id)
            rates = {r["meter"]: r["amount"] for r in model["usage_prices"]["rules"][0]["rates"]}
            self.assertEqual(rates, {"input_uncached_tokens": "10", "input_cached_tokens": cache,
                                     "output_tokens": "50", "cache_write_5m_tokens": "12.5"})


if __name__ == "__main__":
    unittest.main()

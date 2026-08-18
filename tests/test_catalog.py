import unittest

from runtime.router import route
from scripts.validate_catalog import main


class CatalogTests(unittest.TestCase):
    def test_catalog_validation(self):
        self.assertEqual(main(), 0)

    def test_empty_intent_has_no_route(self):
        self.assertEqual(route(""), [])

    def test_creative_intent_routes_to_creative_director(self):
        results = route("manga image storyboard")
        self.assertEqual(results[0]["agent_id"], "avatararts.creative-director")

    def test_required_capability_filters_candidates(self):
        results = route("creative work", ["narrative-design"])
        self.assertEqual([item["agent_id"] for item in results], ["avatararts.creative-director"])

    def test_order_is_deterministic(self):
        self.assertEqual(route("verification testing"), route("verification testing"))


if __name__ == "__main__":
    unittest.main()

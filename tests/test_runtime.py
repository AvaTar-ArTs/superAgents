import unittest

from runtime.envelope import build_event, build_execution
from runtime.policy import evaluate


class RuntimeTests(unittest.TestCase):
    def test_low_risk_read_is_allowed(self):
        result = evaluate("read", "low")
        self.assertEqual(result["decision"], "allow")

    def test_medium_create_requires_confirmation(self):
        result = evaluate("create", "medium")
        self.assertEqual(result["decision"], "confirm")
        self.assertEqual(evaluate("create", "medium", confirmed=True)["decision"], "allow")

    def test_denied_action_wins_over_confirmation(self):
        self.assertEqual(evaluate("charge", "high", confirmed=True)["decision"], "deny")

    def test_execution_and_event_have_linked_ids(self):
        execution = build_execution("research sources", "superagents.verifier", ["research.source-backed"])
        event = build_event(execution["execution_id"], "route_selected", "router")
        self.assertEqual(event["execution_id"], execution["execution_id"])

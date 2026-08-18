import json
import tempfile
import unittest
from pathlib import Path

from scripts.sync_agent_skills_catalog import sync


class SyncTests(unittest.TestCase):
    def test_sync_accepts_list_export(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.json"
            output = root / "output.json"
            source.write_text(json.dumps([{"name": "Demo Skill", "tags": ["demo"]}]))
            self.assertEqual(sync(source, output, "demo"), 1)
            result = json.loads(output.read_text())
            self.assertEqual(result["skills"][0]["id"], "demo-skill")
            self.assertEqual(result["skills"][0]["source"], "demo:demo-skill")

    def test_sync_accepts_wrapped_export(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.json"
            output = root / "output.json"
            source.write_text(json.dumps({"skills": [{"id": "wrapped.skill", "name": "Wrapped"}]}))
            self.assertEqual(sync(source, output, "demo"), 1)
            self.assertEqual(json.loads(output.read_text())["skills"][0]["id"], "wrapped.skill")


if __name__ == "__main__":
    unittest.main()

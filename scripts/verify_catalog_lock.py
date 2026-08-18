#!/usr/bin/env python3
"""Verify the generated catalog against its lockfile."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    lock_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("manifests/catalog.lock.json")
    manifest_path = Path("manifests/skills.json")
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    manifest_bytes = manifest_path.read_bytes()
    expected = lock["generated_manifest"]["sha256"]
    actual = hashlib.sha256(manifest_bytes).hexdigest()
    if actual != expected:
        raise SystemExit(f"manifest hash mismatch: expected {expected}, got {actual}")
    datetime.fromisoformat(lock["generated_at"].replace("Z", "+00:00")).astimezone(timezone.utc)
    for source in lock["sources"]:
        if not re.fullmatch(r"[0-9a-f]{40}", source["commit"]):
            raise SystemExit(f"source commit is not pinned: {source['commit']}")
        if not re.fullmatch(r"[0-9a-f]{64}", source["sha256"]):
            raise SystemExit(f"source export hash is invalid: {source['sha256']}")
    print(f"lock valid: {lock_path}; manifest sha256 {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

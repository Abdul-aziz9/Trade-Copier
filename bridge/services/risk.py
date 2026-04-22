from __future__ import annotations

from typing import Optional, Tuple


def check_risk(event: dict) -> Tuple[bool, Optional[str]]:
    """
    Stage 1 stub:
    Always allow. This keeps risk integrated in the pipeline
    without blocking execution during initial build/testing.
    """
    return True, None
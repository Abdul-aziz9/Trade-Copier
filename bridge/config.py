from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "configs"
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "copier.db"


def load_json(filename: str) -> Any:
    path = CONFIG_DIR / filename
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


ACCOUNTS: Dict[str, Any] = load_json("accounts.json")
SYMBOLS: List[Dict[str, Any]] = load_json("symbols.json")

APP_CONFIG = {
    "host": "127.0.0.1",
    "port": 8000,
    "db_path": str(DB_PATH),
}
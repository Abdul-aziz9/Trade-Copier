from __future__ import annotations

from typing import Dict

from config import SYMBOLS


def map_symbol(source_symbol: str, target_platform: str) -> str:
    for row in SYMBOLS:
        if row["source"].upper() == source_symbol.upper():
            mapped = row.get(target_platform)
            if mapped:
                return mapped
    raise ValueError(f"No symbol mapping found for {source_symbol} -> {target_platform}")
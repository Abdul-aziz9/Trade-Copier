from __future__ import annotations

from typing import Any, Dict, Optional

from config import ACCOUNTS


class TradeLockerConnector:
    """
    Stage 1 stub connector.

    Replace the placeholder request logic with real HTTP calls after
    confirming your exact TradeLocker demo credentials and endpoints.
    """

    def __init__(self) -> None:
        self.config = ACCOUNTS["tradelocker"]
        self.token: Optional[str] = None

    def login(self) -> str:
        # TODO: Replace with real auth flow
        self.token = "demo-tradelocker-token"
        return self.token

    def health_check(self) -> str:
        return "connected" if self.token else "not_authenticated"

    def place_market_order(
        self,
        symbol: str,
        side: str,
        volume: float,
        sl: float | None,
        tp: float | None,
    ) -> Dict[str, Any]:
        if not self.token:
            self.login()

        return {
            "ok": True,
            "platform": "tradelocker",
            "target_order_id": f"tl-order-{symbol}-{side}-{volume}",
            "target_position_id": f"tl-position-{symbol}-{side}",
            "status": "OPENED",
        }

    def close_position(self, target_position_id: str) -> Dict[str, Any]:
        if not self.token:
            self.login()

        return {
            "ok": True,
            "platform": "tradelocker",
            "target_order_id": None,
            "target_position_id": target_position_id,
            "status": "CLOSED",
        }

    def modify_sl_tp(
        self,
        target_position_id: str,
        sl: float | None,
        tp: float | None,
    ) -> Dict[str, Any]:
        if not self.token:
            self.login()

        return {
            "ok": True,
            "platform": "tradelocker",
            "target_order_id": None,
            "target_position_id": target_position_id,
            "status": "MODIFIED",
        }
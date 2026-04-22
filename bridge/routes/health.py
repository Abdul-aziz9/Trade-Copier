from fastapi import APIRouter

from connectors.dxtrade import DXTradeConnector
from connectors.tradelocker import TradeLockerConnector

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health() -> dict:
    tl = TradeLockerConnector()
    dx = DXTradeConnector()

    # Stage 1: attempt login so health becomes useful
    tl.login()
    dx.login()

    return {
        "status": "ok",
        "tradelocker": tl.health_check(),
        "dxtrade": dx.health_check(),
    }
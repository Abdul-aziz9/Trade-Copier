from fastapi import APIRouter

from connectors.dxtrade import DXTradeConnector
from connectors.tradelocker import TradeLockerConnector

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health() -> dict:
    tl = TradeLockerConnector()
    dx = DXTradeConnector()

    return {
        "status": "ok",
        "tradelocker": tl.health_check(),
        "dxtrade": dx.health_check(),
    }
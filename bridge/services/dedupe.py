from db import event_exists


def is_duplicate(event_id: str) -> bool:
    return event_exists(event_id)
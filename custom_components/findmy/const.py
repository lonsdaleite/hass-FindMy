"""Integration constants."""

DOMAIN = "findmy"

CONF_AWAY_TIMEOUT = "away_timeout"
DEFAULT_AWAY_TIMEOUT_MINUTES = 10


def signal_local_observation(unique_id: str) -> str:
    """Dispatcher signal fired when a rolling accessory is matched locally."""
    return f"{DOMAIN}_local_observation_{unique_id}"

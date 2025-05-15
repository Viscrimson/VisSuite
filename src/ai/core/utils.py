# Common utility functions for AI logic

def format_timestamp(ts) -> str:
    """Convert timestamp to human-readable string."""
    from datetime import datetime
    return datetime.fromtimestamp(ts).isoformat()
import sqlite3
import logging

logger = logging.getLogger(__name__)

class ConvoLogger:
    """Log conversations to SQLite for context recall."""
    def __init__(self, db_path: str = 'logs/convo.db') -> None:
        self.conn = sqlite3.connect(db_path)
        # TODO: initialize tables

    def append(self, speaker: str, text: str) -> None:
        """Insert timestamped message into log."""
        raise NotImplementedError("ConvoLogger.append not implemented yet")
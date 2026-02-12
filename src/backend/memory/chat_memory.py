"""Chat memory management with SQLite persistence."""

import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver


class ChatMemoryManager:
    """Manage chat history and checkpoints using SQLite."""

    def __init__(
        self,
        db_path: str = "/Users/mukul/Desktop/Chatbot/src/backend/memory/chat_history.db",
    ):
        """Initialize the chat memory manager."""
        self.db_path = db_path
        self.connector = sqlite3.connect(db_path, check_same_thread=False)
        self.checkpointer = SqliteSaver(conn=self.connector)

    def get_checkpointer(self):
        """Return the checkpointer instance."""
        return self.checkpointer

    def close(self):
        """Close the database connection."""
        self.connector.close()

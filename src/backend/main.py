"""Logic connection - Main backend orchestration."""

from langchain_core.messages import HumanMessage
from src.backend.workflow.main_workflow import create_chatbot_workflow
from src.backend.memory.chat_memory import ChatMemoryManager


class ChatbotApp:
    """Main chatbot application."""

    def __init__(
        self,
        db_path: str = "/Users/mukul/Desktop/Chatbot/src/backend/memory/chat_history.db",
        thread_id: str = "default",
    ):
        """Initialize the chatbot application."""
        self.memory_manager = ChatMemoryManager(db_path)
        self.workflow = create_chatbot_workflow(self.memory_manager.get_checkpointer())
        self.thread_id = thread_id
        self.config = {"configurable": {"thread_id": self.thread_id}}

    def process_query(self, user_query: str):
        """Process user query and return AI response."""
        for message_chunk, metadata in self.workflow.stream(
            {"messages": [HumanMessage(content=user_query)]},
            stream_mode="messages",
            config=self.config,
        ):
            if message_chunk.content:
                yield message_chunk.content

    def close(self):
        """Clean up resources."""
        self.memory_manager.close()

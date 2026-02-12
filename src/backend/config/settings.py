"""Configuration management for the chatbot."""

import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()


class ChatbotSettings:
    """Chatbot configuration settings."""

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_BASE_URL = os.getenv("MODEL_BASE_URL")
    # TEMPERATURE = float(os.getenv("TEMPERATURE"))

    @staticmethod
    def get_llm():
        """Initialize and return LLM instance."""
        return ChatOpenAI(
            api_key=ChatbotSettings.OPENAI_API_KEY,
            base_url=ChatbotSettings.MODEL_BASE_URL,
        )


# response = ChatbotSettings.get_llm().invoke("hello")
# print(response.content)

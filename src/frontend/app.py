"""Gradio web interface - main chatbot application logic."""

import gradio as gr
from src.backend.main import ChatbotApp


def create_gradio_interface():
    """Create and configure Gradio interface."""
    chatbot_app = ChatbotApp(thread_id="5")

    def chat_interface(message, history):
        """Handle chat messages."""
        response = ""
        for chunk in chatbot_app.process_query(message):
            response += chunk
            yield response

    demo = gr.ChatInterface(chat_interface, title="Agentic Chatbot")
    return demo, chatbot_app


if __name__ == "__main__":
    demo, app = create_gradio_interface()
    demo.launch()

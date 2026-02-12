"""Conversation chains and workflow orchestration."""

from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage
from src.backend.config.settings import ChatbotSettings


class ChatbotState(TypedDict):
    """State schema for chatbot workflow."""

    messages: Annotated[list[BaseMessage], add]


def create_chatbot_workflow(checkpointer=None):
    """Create and compile the chatbot workflow graph."""
    llm = ChatbotSettings.get_llm()

    def llm_response(state: ChatbotState):
        """Process messages through LLM."""
        messages = state["messages"]
        complete_response = llm.invoke(messages)
        return {"messages": [complete_response]}

    graph = StateGraph(state_schema=ChatbotState)
    graph.add_node("llm_response", llm_response)
    graph.add_edge(START, "llm_response")
    graph.add_edge("llm_response", END)

    return graph.compile(checkpointer=checkpointer)

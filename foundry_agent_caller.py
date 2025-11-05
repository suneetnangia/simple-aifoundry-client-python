"""
AI Foundry Agent Caller using Default Azure Credentials

This module provides a simple interface to call an AI Foundry agent
using Azure Default Credentials for authentication.
"""

import json
from pathlib import Path

from azure.ai.agents.models import AgentThread, ListSortOrder
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential


class FoundryAgentCaller:
    """Call an AI Foundry agent with default Azure credentials."""

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the Foundry Agent Caller.

        Args:
            config_path: Path to the configuration file containing endpoint and agent ID
        """
        self.config = self._load_config(config_path)
        self.endpoint = self.config["endpoint"]
        self.agent_id = self.config["agent_id"]

        # Initialize Azure credential
        self.credential = DefaultAzureCredential()

        # Initialize AI Project Client
        self.client = AIProjectClient(
            endpoint=self.endpoint,
            credential=self.credential,
        )

    def _load_config(self, config_path: str) -> dict:
        """Load configuration from JSON file."""
        config_file = Path(config_path)
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

        with open(config_file) as f:
            return json.load(f)

    def create_thread(self) -> AgentThread:
        """
        Create a new conversation thread.

        Returns:
            AgentThread: The created thread object
        """
        thread = self.client.agents.threads.create()
        print(f"Created thread with ID: {thread.id}")
        return thread

    def send_message(self, thread_id: str, message: str, agent_id: str | None = None) -> str:
        """
        Send a message to the agent in a thread.

        Args:
            thread_id: The ID of the thread to send the message to
            message: The message content to send
            agent_id: Optional agent ID. If not provided, uses agent_id from config

        Returns:
            str: The agent's response text
        """
        # Create message in thread
        self.client.agents.messages.create(thread_id=thread_id, role="user", content=message)
        print(f"Sent message: {message}")

        # Run the agent
        if agent_id is None:
            agent_id = self.agent_id

        run = self.client.agents.runs.create_and_process(thread_id=thread_id, agent_id=agent_id)
        print(f"Run completed with status: {run.status}")

        if run.status == "failed":
            raise RuntimeError(f"Run failed: {run.last_error}")

        # Get messages
        messages = self.client.agents.messages.list(
            thread_id=thread_id, order=ListSortOrder.ASCENDING
        )

        # Return the latest assistant message text
        for msg in messages:
            if msg.role == "assistant" and msg.text_messages:
                return msg.text_messages[-1].text.value

        raise RuntimeError("No assistant response found")

    def chat(self, user_message: str, thread_id: str | None = None) -> str:
        """
        Simple chat interface - send a message and get a response.

        Args:
            user_message: The message to send to the agent
            thread_id: Optional thread ID. If not provided, creates a new thread

        Returns:
            str: The agent's response text
        """
        # Create thread if not provided
        if thread_id is None:
            thread = self.create_thread()
            thread_id = thread.id

        # Send message and get response
        response_text = self.send_message(thread_id, user_message)

        return response_text


def main():
    """Example usage of the Foundry Agent Caller."""
    try:
        # Initialize the caller
        caller = FoundryAgentCaller()

        # Example: Simple one-off chat
        print("\n=== Single Message Example ===")
        response = caller.chat("Hello! Can you help me with Python programming?")
        print(f"\nAgent Response:\n{response}")

        # Example: Multi-turn conversation
        print("\n\n=== Multi-turn Conversation Example ===")
        thread = caller.create_thread()

        messages = [
            "What is Azure AI Foundry?",
            "What are its main features?",
            "How do I get started?",
        ]

        for msg in messages:
            print(f"\n>>> User: {msg}")
            response = caller.chat(msg, thread_id=thread.id)
            print(f">>> Agent: {response}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please create a config.json file with your endpoint and agent_name")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

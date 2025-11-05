"""
Simple example of calling an AI Foundry agent.

Before running:
1. Update config.json with your AI Foundry endpoint and agent name
2. Ensure you're authenticated with Azure (az login or set environment variables)
3. Install dependencies: pip install -r requirements.txt
"""

from foundry_agent_caller import FoundryAgentCaller


def simple_chat_example():
    """Simple example: Send a single message and get a response."""
    # Initialize the caller with config.json
    caller = FoundryAgentCaller()

    # Send a message and get a response
    response = caller.chat("Show me the EPS values from the file.")

    print(f"Agent Response:\n{response}")


def multi_turn_conversation_example():
    """Example: Have a multi-turn conversation with the agent."""
    # Initialize the caller
    caller = FoundryAgentCaller()

    # Create a thread for the conversation
    thread = caller.create_thread()

    # Have a conversation
    questions = ["Show me the EPS from the file.", "Show me the adjusted EPS only now."]

    for question in questions:
        print(f"\n>>> User: {question}")
        response = caller.chat(question, thread_id=thread.id)
        print(f">>> Agent: {response}\n")
        print("-" * 80)


if __name__ == "__main__":
    print("Choose an example:")
    print("1. Simple chat (single message)")
    print("2. Multi-turn conversation")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        simple_chat_example()
    elif choice == "2":
        multi_turn_conversation_example()
    else:
        print("Invalid choice. Running simple chat example...")
        simple_chat_example()

# AI Foundry Agent Caller

A simple Python project to call agents in Azure AI Foundry using Default Azure Credentials.

## Features

- Uses Azure Default Credentials for authentication (no hardcoded credentials needed)
- Configurable endpoint via `config.json`
- Simple chat interface for single messages
- Support for multi-turn conversations with threads
- Clean, modular code structure

## Prerequisites

- Python 3.10 or higher
- Azure subscription with AI Foundry access
- An AI Foundry agent deployed and ready to use

## Installation

1. Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Copy and update `config.json` with your settings:

```json
{
  "endpoint": "https://your-project.api.azureml.ms",
  "agent_id": "your-agent-id"
}
```

- `endpoint`: Your AI Foundry project endpoint
- `agent_id`: The ID of your deployed agent (e.g., "asst_abc123...")

## Authentication

This project uses Azure Default Credentials, which automatically tries multiple authentication methods:

1. Environment variables (AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET)
2. Managed Identity (if running in Azure)
3. Azure CLI (`az login`)
4. Azure PowerShell
5. Interactive browser login

### Quick Authentication Setup

The easiest way to authenticate locally:

```bash
az login
```

## Usage

### Simple Example

```python
from foundry_agent_caller import FoundryAgentCaller

# Initialize with config.json
caller = FoundryAgentCaller()

# Send a message and get a response
response = caller.chat("Hello! What can you help me with?")
print(response)
```

### Multi-turn Conversation

```python
from foundry_agent_caller import FoundryAgentCaller

# Initialize
caller = FoundryAgentCaller()

# Create a thread for the conversation
thread = caller.create_thread()

# Have a conversation
response1 = caller.chat("What is Azure AI?", thread_id=thread.id)
response2 = caller.chat("Tell me more about it", thread_id=thread.id)
```

### Running the Examples

Run the included example file:

```bash
python example.py
```

Or run the main module:

```bash
python foundry_agent_caller.py
```

## Project Structure

```
.
├── config.json                 # Configuration file (endpoint, agent ID)
├── foundry_agent_caller.py    # Main module with FoundryAgentCaller class
├── example.py                  # Simple usage examples
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## API Reference

### FoundryAgentCaller

Main class for interacting with AI Foundry agents.

#### Methods

- `__init__(config_path: str = "config.json")` - Initialize the caller with configuration
- `create_thread() -> AgentThread` - Create a new conversation thread
- `send_message(thread_id: str, message: str, agent_id: Optional[str] = None) -> ThreadMessage` - Send a message to the agent
- `get_message_text(message: ThreadMessage) -> str` - Extract text from a message
- `chat(user_message: str, thread_id: Optional[str] = None) -> str` - Simple chat interface

## Troubleshooting

### Authentication Errors

If you see authentication errors:

1. Make sure you're logged in: `az login`
2. Verify you have access to the AI Foundry resource
3. Check that your Azure subscription is active

### Configuration Errors

If you see "Configuration file not found":

1. Make sure `config.json` exists in the same directory
2. Verify the JSON syntax is correct
3. Update the endpoint and agent_id values (agent_id typically starts with "asst_")

### Connection Errors

If you can't connect to the endpoint:

1. Verify the endpoint URL is correct
2. Check that the AI Foundry project is running
3. Ensure your network allows connections to Azure

## Dependencies

- `azure-ai-projects` - Azure AI Projects SDK
- `azure-ai-agents-persistent` - Azure AI Agents with persistence
- `azure-identity` - Azure authentication library

## License

This project is provided as-is for demonstration purposes.


# Sherlock MCP 
[![smithery badge](https://smithery.ai/badge/@qKitNp/sherlock_mcp)](https://smithery.ai/server/@qKitNp/sherlock_mcp) [![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/9a7df53f-dece-40c1-8819-beb0cf73e960)


A FastMCP-based tool for searching usernames across multiple social media platforms using Sherlock. This tool provides both standard and NSFW platform search capabilities.

## Features

- Search for usernames across multiple social media platforms
- Support for both standard and NSFW platform searches
- Simple API interface for integration with other applications
- Built with FastMCP for efficient request handling

## Prerequisites

- Python 3.7+
- FastMCP
- Sherlock

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sherlock_mcp.git
   cd sherlock_mcp
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

Start the MCP server:
```bash
python main.py
```

### Making Requests

Use the included `server.py` as an example of how to interact with the service:

```python
import asyncio
from fastmcp import Client

client = Client("main.py")

async def call_tool(name):
    async with client:
        # For standard search
        result = await client.call_tool("get_links", {"username": name})
        print("Standard results:", result)
        
        # For NSFW search
        nsfw_result = await client.call_tool("get_nsfw_links", {"username": name})
        print("NSFW results:", nsfw_result)

name = input("Enter username: ")
asyncio.run(call_tool(name))
```

## Available Endpoints

- `get_links(username: str)`: Search for a username across standard social media platforms
- `get_nsfw_links(username: str)`: Search for a username including NSFW platforms

## Response Format

Both endpoints return a JSON string containing an array of objects with the following structure:

```json
[
    {
        "site": "Platform Name",
        "url": "https://platform.com/username"
    },
    ...
]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

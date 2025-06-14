import asyncio
from fastmcp import Client

client = Client("main.py")

async def call_tool(name):
    async with client:
        result = await client.call_tool("get_links", {"username": name})
        print(result)


name = input("Enter username: ")
asyncio.run(call_tool(name))
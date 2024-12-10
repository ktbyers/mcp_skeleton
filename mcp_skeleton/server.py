from typing import Any

import mcp.types as types
from mcp.server import Server
from mcp.types import Resource, Tool

server = Server(name="my-server")

@server.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    pass

@server.get_prompt()
async def handle_get_prompt(
    name: str,
    arguments: dict[str, str] | None
) -> types.GetPromptResult:
    pass

@server.list_resources()
async def list_resources() -> list[Resource]:
    pass

@server.read_resource()
async def read_resource(uri) -> str:
    pass

@server.list_tools()
async def list_tools() -> list[Tool]:
    pass

@server.call_tool()
async def call_tool(
    name: str, arguments: Any
):
    pass

async def main():
    """Run the main async event loop."""
    # Import here to avoid issues with event loops -- WHY?
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

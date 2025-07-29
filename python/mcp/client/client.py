import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    # check your running Function MCP Server, it will output where its available
    # at during initialization.
    async with streamablehttp_client("http://localhost:8080/mcp") as streams:
        read_stream,write_stream = streams[0],streams[1]

        async with ClientSession(read_stream,write_stream) as s:
            print("Initializing connection...",end="")
            await s.initialize()
            print("done!\n")

            # List all available tools
            #tools = await s.list_tools()
            #print("--- List of tools ---")
            #print(tools.tools)

            # Call hello tool which will greet Thomas
            hello_tool = await s.call_tool(
                name="hello_tool",
                arguments={"name": "Thomas"}
                )

            # Print the actual content of the result
            print(hello_tool.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())

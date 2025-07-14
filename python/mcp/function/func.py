# function/func.py

# Function as an MCP Server implementation
import logging

from mcp.server.fastmcp import FastMCP
import asyncio

def new():
    """ New is the only method that must be implemented by a Function.
    The instance returned can be of any name.
    """
    return Function()

class MCPServer:
    """MCP server that exposes tools, resources, and prompts via the MCP protocol."""

    def __init__(self):
        # Create FastMCP instance with stateless HTTP for Kubernetes deployment
        self.mcp = FastMCP("Function MCP Server", stateless_http=True)

        self._register_tools()
        #self._register_resources()
        #self._register_prompts()

        # Get the ASGI app from FastMCP
        self._app = self.mcp.streamable_http_app()

    def _register_tools(self):
        """Register MCP tools."""
        @self.mcp.tool()
        def hello_tool(name: str) -> str:
            """Say hello to someone."""
            return f"Hey there {name}!"

        @self.mcp.tool()
        def add_numbers(a: int, b: int) -> int:
            """Add two numbers together."""
            return a + b

## Other MCP objects include resources and prompts.
## Add them here to be registered in the same fashion as tools above.
#    def _register_resources(self):
#        """Register MCP resources."""
#        @self.mcp.resource("echo://{message}")
#        def echo_resource(message: str) -> str:
#            """Echo the message as a resource."""
#            return f"Echo: {message}"
#
#    def _register_prompts(self):
#        """Register MCP prompts."""
#        @self.mcp.prompt()
#        def greeting_prompt(name: str = "Big Dave"):
#            """Generate a greeting prompt."""
#            return [
#                {
#                    "role": "user",
#                    "content": f"Please write a friendly greeting for {name}"
#                }
#            ]

    async def handle(self, scope, receive, send):
        """Handle ASGI requests - both lifespan and HTTP."""
        await self._app(scope, receive, send)

class Function:
    def __init__(self):
        """ The init method is an optional method where initialization can be
        performed. See the start method for a startup hook which includes
        configuration.
        """
        self.mcp_server = MCPServer()
        self._mcp_initialized = False

    async def handle(self, scope, receive, send):
        """
        Main entry to your Function.
        This handles all the incoming requests.
        """

        # Initialize MCP server on first request
        if not self._mcp_initialized:
            await self._initialize_mcp()

        # Route MCP requests
        if scope['path'].startswith('/mcp'):
            await self.mcp_server.handle(scope, receive, send)
            return

        # Default response for non-MCP requests
        await self._send_default_response(send)

    async def _initialize_mcp(self):
        """Initialize the MCP server by sending lifespan startup event."""
        lifespan_scope = {'type': 'lifespan', 'asgi': {'version': '3.0'}}
        startup_sent = False

        async def lifespan_receive():
            nonlocal startup_sent
            if not startup_sent:
                startup_sent = True
                return {'type': 'lifespan.startup'}
            await asyncio.Event().wait()  # Wait forever for shutdown

        async def lifespan_send(message):
            if message['type'] == 'lifespan.startup.complete':
                self._mcp_initialized = True
            elif message['type'] == 'lifespan.startup.failed':
                logging.error(f"MCP startup failed: {message}")

        # Start lifespan in background
        asyncio.create_task(self.mcp_server.handle(
            lifespan_scope, lifespan_receive, lifespan_send
        ))

        # Brief wait for startup completion
        await asyncio.sleep(0.1)

    async def _send_default_response(self, send):
        """
        Send default OK response.
        This is for your non MCP requests if desired.
        """
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [[b'content-type', b'text/plain']],
        })
        await send({
            'type': 'http.response.body',
            'body': b'OK',
        })

    def start(self, cfg):
        logging.info("Function starting")

    def stop(self):
        logging.info("Function stopping")

    def alive(self):
        return True, "Alive"

    def ready(self):
        return True, "Ready"

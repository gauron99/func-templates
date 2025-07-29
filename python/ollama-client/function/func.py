# Function
import logging
from ollama import Client
import json
import os

def new():
    """ New is the only method that must be implemented by a Function.
    The instance returned can be of any name.
    """
    return Function()

# helper function for sending responses
async def send_it(send,msg:str|None):
    if msg == None:
        msg = ""

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': msg.encode(),
    })

class Function:
    def __init__(self):
        """ The init method is an optional method where initialization can be
        performed. See the start method for a startup hook which includes
        configuration.
       """
        self.client = Client(
                # where your OLLAMA server is running
                host=os.environ.get("OLLAMA_HOST","127.0.0.1:11434")
                )

    async def handle(self, scope, receive, send):
        """ Handle all HTTP requests to this Function other than readiness
        and liveness probes.

        To communicate with the LLM following curl data is expected:
            {
                "prompt":"Your prompt for LLM",
                "model": "Your preffered ollama-compatible model",
            }

            Note: Both of these have defaults, therefore you dont need to
            provide them.

            example: curl <host:port> -d '{"prompt":"What is philosophy exactly"}'
             """
        logging.info("OK: Request Received")

        if scope["method"] == "GET":
            await send_it(send,'OK')
            return

        # 1) extract the whole body from request
        body = b''
        more_body = True
        while more_body:
            message = await receive()
            body += message.get('body', b'')
            more_body = message.get('more_body', False)

        # 2) decode the request and fetch info
        data = json.loads(body.decode('utf-8'))
        prompt = data.get('prompt','Who are you?')
        model = data.get('model',"llama3.2:1b")

        print(f"using model {model}")
        # 3) make /api/chat request to the ollama server
        response = self.client.chat(
                # assign your model here
                model=model,
                messages=[
                    {
                    'role':'user',
                    'content':prompt,
                    },
                ])

        # 4) return the response to the calling client
        await send_it(send,response.message.content)

    def start(self, cfg):
        """ start is an optional method which is called when a new Function
        instance is started, such as when scaling up or during an update.
        Provided is a dictionary containing all environmental configuration.
        Args:
            cfg (Dict[str, str]): A dictionary containing environmental config.
                In most cases this will be a copy of os.environ, but it is
                best practice to use this cfg dict instead of os.environ.
        """
        logging.info("Function starting")

    def stop(self):
        """ stop is an optional method which is called when a function is
        stopped, such as when scaled down, updated, or manually canceled.  Stop
        can block while performing function shutdown/cleanup operations.  The
        process will eventually be killed if this method blocks beyond the
        platform's configured maximum studown timeout.
        """
        logging.info("Function stopping")

    def alive(self):
        """ alive is an optional method for performing a deep check on your
        Function's liveness.  If removed, the system will assume the function
        is ready if the process is running. This is exposed by default at the
        path /health/liveness.  The optional string return is a message.
        """
        return True, "Alive"

    def ready(self):
        """ ready is an optional method for performing a deep check on your
        Function's readiness.  If removed, the system will assume the function
        is ready if the process is running.  This is exposed by default at the
        path /health/rediness.
        """
        return True, "Ready"

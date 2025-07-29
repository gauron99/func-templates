# Function
import logging
from llama_cpp import Llama
import json

def new():
    """ New is the only method that must be implemented by a Function.
    The instance returned can be of any name.
    """
    return Function()

class Function:
    def __init__(self):
        """ The init method is an optional method where initialization can be
        performed. See the start method for a startup hook which includes
        configuration.
        """

    async def sender(self,send,obj):
        # echo the obj to the calling client
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': obj.encode(),
        })

    async def handle(self, scope, receive, send):
        """
        accepts data in form of JSON with the key "input" which should
        contain the input string for the LLM
        {
            "input": "this is passed to the LLM"
        }
        ex: curl localhost:8080 -d '{"input":"The largest mountain in the world is"}'
        """
        if scope["method"] == "GET":
            await self.sender(send,"OK")
            return

        input = ""

        # fetch all of the body from request
        body = b''
        more_body = True
        while more_body:
            message = await receive()
            body += message.get('body', b'')
            more_body = message.get('more_body', False)
        # decode json
        try:
            data = json.loads(body.decode('utf-8'))
            input = data['input']
        except json.JSONDecodeError:
            ret = "Invalid Json"
        except KeyError:
            ret = "invalid key, expected 'input'"

        if input == "":
            self.sender(send,"OK")

        # Pull model from Hugging Face Hub
        llm = Llama.from_pretrained(
            repo_id="ibm-granite/granite-3b-code-base-2k-GGUF",
            filename="granite-3b-code-base.Q4_K_M.gguf",
            n_ctx=1024,
        )

       ## Use a local image instead
       #llm = Llama (
       #     model_path = "/granite-7b-lab-Q4_K_M.gguf/snapshots/sha256-6adeaad8c048b35ea54562c55e454cc32c63118a32c7b8152cf706b290611487/granite-7b-lab-Q4_K_M.gguf",
       #     n_ctx = 1024,
       # )

        output = llm(
            input,
            max_tokens=32,
            ## Stop generating just before "Q:"; doesnt work well with small models
            ## some models are more tuned to the Q: ... A: ... "chat"
            ## You would literally type that in your input as: f' Q: {input}. A:'
            #stop=["Q:","\n"],
            echo=False,
        )
        #logging.info("------------")
        #logging.info(output['choices'][0]['text'])
        await self.sender(send,output['choices'][0]['text'])

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

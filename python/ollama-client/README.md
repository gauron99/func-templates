# Python Ollama-Client Function (HTTP)

Welcome to your Python Ollama Client Function. It uses the [ollama](https://github.com/ollama/ollama)
library.

## The Function

Your Function can be found in `function/func.py`. It handles HTTP requests in
the `handle(self,scope,receive,send)` which is also the ASGI's handle signature
(It's ASGI compatible). The only requests handled elsewhere are readiness and
liveness checks -- `ready` and `alive` functions respectivelly.

### What it does

During initialization, we set a the Ollama's client with the correct server
adress. That's it. Everything else happens in the `handle` function itself.

`handle` function includes some error handling and simple http body extraction
and subsequently it makes an API request to the ollama server using Ollama's
`client.chat()` function.

### Expected data

Any `GET` request will simply echo the standard 'OK' string.

`POST` request should be in json format and include `prompt` key. This is your
prompt for the LLM. Additionally you can include `model` key which is the name
of the model you want to use.

Example of a curl command:

```bash
# use the default model
curl localhost:11434 -d '{"prompt":"How to cook eggs properly?"}'

# use different model
curl localhost:11434 -d '{"prompt":"How to cook eggs properly?","model":"llama3.2:3b"}'
```

These values are simply extracted from the request and if provided it feeds them
to the request for the LLM in a ollama complient way (see the construction of
`self.client.chat()` function call).

## Extra

As per usual, the Function also contains a readiness and liveness checks
implemented at the bottom of the Function class in their matching function names.
The `start` and `stop` function are also available. See the function comments
for more descriptive information.

For more info about the Ollama library, please visit [ollama github page](https://github.com/ollama/ollama)

For more info about Functions, see [the complete documentation]('https://github.com/knative/func/tree/main/docs')

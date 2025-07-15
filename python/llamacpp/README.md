# Python Llama_cpp Function (HTTP)

Welcome to your Llama-cpp Function which integrates a basic client side structure
of the [Llama-cpp library](). The Function accepts JSON input which it processes
through a local LLM and returns the generated response.

The Function itself uses ASGI protocol.

## Deployment

> [!Note]
> We recommend using the host builder

```bash
#Run the function locally
func run --builder=host

#Deploy to clustert
func deploy --builder=host
```

## How to use the API

The Function accepts POST requests with JSON data. You can create a request like
this:
```bash
curl localhost:8080 -d '{"input":"The largest mountain in the world is"}'
```

GET requests return 'OK' string for a quick check.

## Customization

- The Function uses the ASGI protocol and is compatible with
`handle(scope,receive,send)` signature.
- You can use a local model (eg: passed through via a base image -- Dockerfile)
by switching the `Llama()` function calls in the `handle()` function for the
commented out code. You will need to provide a path to the model via `model_path`
argument instead of a `repo_id` and `filename`.
- As per usual, the Function implements a readiness and liveness checks as well
as start and stop methods implemented via functions matching their names
respectivelly. These can be found at the bottom of the Function class with more
detailed information in the comments.

## Tests

Tests use the `pytest` framework with asyncio.

The function tests can be found in `tests` directory. It contains a simple
http request test. This is where you can create your own tests for desired
functionality.

```bash
#Install dependencies (if not done already)
pip install -e .

# Run the tests
pytest

# Run verbosely
pytest -v
```

## Dependencies

All dependencies can be found in the `pyproject.toml` file. Any additional
dependencies (eg: A model when running locally) can be also provided via the
mentioned base image. You can create a Dockerfile like so:

```Dockerfile
FROM python3.13:slim
## RUN any bash commands for pip install etc.
COPY /path/to/model/on/host/machine /path/to/model/in/container
```

You will build this image for example using podman and then pass it into the
Function when building it via `--base-image` flag.
```bash
# build my base image
podman build -f Dockerfile -t my-base-image

# use the base image when building my Function image
func build --base-image=localhost/my-base-image --builder=host

# or deploy immediately (builds internally)
func deploy --base-image=localhost/my-base-image --builder=host
```

which will make the model accesible for the Function.

For more, see [the complete documentation]('https://github.com/knative/func/tree/main/docs')

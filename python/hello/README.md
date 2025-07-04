# Python HTTP Function

## Introduction

A Python HTTP function built with ASGI protocol support. The implementation 
provides a simple HTTP endpoint that responds with "Hello World!" to incoming 
requests.

The function is structured as a class-based implementation with proper lifecycle
management, including configurable startup and shutdown hooks.

## Recommended Deployment

> [!NOTE]
> We recommend using the host builder.
> This feature is currently behind a flag because its not available for all the
> languages yet so you will need to enable it.

```bash
# Enable the host builder
export FUNC_ENABLE_HOST_BUILDER=1

# Deploy your code to cluster
# Make sure to set the builder to use it
func deploy --builder=host

# Local development and testing
func run --builder=host --container=false
```

## Customization

- This function uses the ASGI (Asynchronous Server Gateway Interface) 3.0
specification therefore its compatible with the signature `handle(scope, receive, send)`

### Lifecycle Management
The function provides lifecycle hooks:
- **start()**: Initialization hook called when function instances are created
- **stop()**: Cleanup hook, ensuring graceful termination and resource cleanup
- **alive()**: Health check exposed at `/health/liveness`
- **ready()**: Readiness check exposed at `/health/readiness`

## Testing

The function includes unit tests that verify the HTTP handler behavior. 
Tests are located in the `tests/` directory and use pytest with asyncio support.

To run the tests:

```bash
# Install dependencies (if not already installed)
pip install -e .

# Run tests
pytest

# Run tests with verbose output
pytest -v
```

### Test Structure

Tests are organized in the `tests/` directory with the current test file 
`test_func.py` verifying that the ASGI handler returns a proper 200 OK response.
The testing framework uses pytest with asyncio support, configured in `pyproject.toml`.

### Writing New Tests

To add new tests, create files named `test_*.py` in the `tests/` directory. 
For async functions, use the `@pytest.mark.asyncio` decorator. Mock ASGI 
components by creating mock `scope`, `receive`, and `send` functions as shown 
in the existing test. You can also test lifecycle methods like `start()`, 
`stop()`, `alive()`, and `ready()` by calling them directly on a function instance.

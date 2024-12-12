# TypeScript HTTP Hello World! Function

Welcome to your new TypeScript function project! The boilerplate function code 
can be found in [`index.ts`](./index.ts). This function will simply print
'Hello World!' on the client side & confirmation of recieving the request on
the server side.

## Local execution

To run locally

```console
npm install
npm run build
npm run start
```

## Testing

This function project includes a [unit test](./test/unit.ts) and an [integration test](./test/integration.ts). Modify these, or add additional tests for your business logic.

```console
npm test
```

## Advanced

### The Function Interface

The `src/index.ts` file may export a single function or a `Function`
object. The `Function` object allows developers to add lifecycle hooks for
initialization and shutdown, as well as providing a way to implement custom
health checks.

The `Function` interface is defined as:

```typescript
export interface Function {
  // The initialization function, called before the server is started
  // This function is optional and should be synchronous.
  init?: () => any;

  // The shutdown function, called after the server is stopped
  // This function is optional and should be synchronous.
  shutdown?: () => any;

  // The liveness function, called to check if the server is alive
  // This function is optional and should return 200/OK if the server is alive.
  liveness?: HealthCheck;

  // The readiness function, called to check if the server is ready to accept requests
  // This function is optional and should return 200/OK if the server is ready.
  readiness?: HealthCheck;

  logLevel?: LogLevel;

  // The function to handle HTTP requests
  handle: CloudEventFunction | HTTPFunction;
}
```

### Handle Signature

The HTTP function interface is defined as:

```typescript
interface HTTPFunction {
  (context: Context, body?: IncomingBody): HTTPFunctionReturn;
}
```

Where the `IncomingBody` is either a string, a Buffer, a JavaScript object, or undefined, depending on what was supplied in the HTTP POST message body. The `HTTTPFunctionReturn` type is defined as:

```typescript
type HTTPFunctionReturn = Promise<StructuredReturn> | StructuredReturn | ResponseBody | void;
```

Where the `StructuredReturn` is a JavaScript object with the following properties:

```typescript
interface StructuredReturn {
  statusCode?: number;
  headers?: Record<string, string>;
  body?: ResponseBody;
}
```

If the function returns a `StructuredReturn` object, then the `statusCode` and `headers` properties are used to construct the HTTP response. If the `body` property is present, it is used as the response body. If the function returns `void` or `undefined`, then the response body is empty.

The `ResponseBody` is either a string, a JavaScript object, or a Buffer. JavaScript objects will be serialized as JSON. Buffers will be sent as binary data.

### Health Checks

The `Function` interface also allows for the addition of a `liveness` and `readiness` function. These functions are used to implement health checks for the function. The `liveness` function is called to check if the function is alive. The `readiness` function is called to check if the function is ready to accept requests. If either of these functions returns a non-200 status code, then the function is considered unhealthy.

A health check function is defined as:

```typescript
/**
 * The HealthCheck interface describes a health check function,
 * including the optional path to which it should be bound.
 */
export interface HealthCheck {
  (request: Http2ServerRequest, reply: Http2ServerResponse): any;
  path?: string;
}
```

By default, the health checks are bound to the `/health/liveness` and `/health/readiness` paths. You can override this by setting the `path` property on the `HealthCheck` object, or by setting the `LIVENESS_URL` and `READINESS_URL` environment variables.

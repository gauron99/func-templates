# Go Splash screen (static webpage)

Welcome to your new Go Function! The function code can be found in
[`function.go`](function.go). This Function is a static web page which will
be server on an available port on localhost (default is 8080 if not occupied).

## Development

Develop new features by adding a test to [`function_test.go`](function_test.go) for
each feature, and confirm it works with `go test`.

Update the running analog of the function using the `func` CLI or client
library, and it can be invoked from your browser or from the command line:

```console
curl http://myfunction.example.com/
```

For more, see [the complete documentation]('https://github.com/knative/func/tree/main/docs')



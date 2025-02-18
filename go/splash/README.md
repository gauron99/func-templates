# Go Splash screen (static webpage)

Welcome to your new Go Function! The function code can be found in
[`function.go`](function.go). This Function is a static web page which
can be run locally with `func run` as well as deployed as usual with
a simple `func deploy` to your existing cluster.

Since the `Handle()` function is exposed, the local files located in root
directory of this function are simply served with `http.ServeFile()`

The Web page includes a `.css` and `.png` files which are both included in your
function (the whole directory is).

If desired, you can uncomment and implement other methods, like Start(),Stop() etc..
All are included in the `function.go` commented out below the `Handle()` method.

## Development

You can develop locally without having the need to redeploy your Function each time
you update your code. Simply execute `func run` in your CLI and develop on
`localhost:8080` (or whatever port is available at the time -- this will be shown
in the CLI).

Hope you enjoy your easy developement and let us know how it goes on [Slack]('https://cloud-native.slack.com/archives/C04LKEZUXEE')

For more, see [the complete documentation]('https://github.com/knative/func/tree/main/docs')



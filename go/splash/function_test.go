package function

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

// TestHandle ensures that the constructor returns the index.html for "/" request
func TestHandle(t *testing.T) {
	var (
		target = "/"
		w      = httptest.NewRecorder()
		req    = httptest.NewRequest(http.MethodGet, target, nil)
		res    *http.Response
	)

	New().Handle(w, req)
	res = w.Result()
	defer res.Body.Close()

	if res.StatusCode != http.StatusOK {
		t.Fatalf("unexpected response code: %v", res.StatusCode)
	}

	if w.Body.String() != expRes {
		t.Fatalf("did not get expected response body for %v, got:\n%v\nexp:\n%v", target, w.Body.String(), expRes)
	}
}

const expRes = `<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Splash screen Function</title>
    <link rel="stylesheet" type="text/css" href="/style.css">
  </head>
  <body>
    <header>
      <h1>Functions Rule!</h1>
        <img src="/logo.png" type="image/png" class="logo" alt="(unoffical)Knative Functions Logo" />
        <p>⮝ Unofficial Func logo ⮝</p>
    </header>
    <div class="content">
        <h3>About</h3>
        <p>This page is served via simple index.html with .css and .png files.
        Everything is handled in the available default 'Handle()' function.
        This means the files in your Function's directory are exposed and accessible.</p>
    </div>
    <footer>
      <p>January 2025</p>
      <p><b>Function for Functions via a Function</b></p>
      <p>~by gauron99</p>
    </footer>

  </body>
</html>
`

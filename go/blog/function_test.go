package function

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

// TestHandle ensures that Handle executes without error and returns the
// HTTP 200 status code indicating no errors.
func TestHandle(t *testing.T) {
	var (
		f   = New()
		w   = httptest.NewRecorder()
		req = httptest.NewRequest("GET", "http://example.com/test", nil)
		res *http.Response
	)
	f.Handle(w, req)
	res = w.Result()
	defer res.Body.Close()

	if res.StatusCode != 200 {
		t.Fatalf("unexpected response code: %v", res.StatusCode)
	}
}

package function

import (
	"fmt"
	"net/http"
)

// Handle an HTTP Request.
func Handle(w http.ResponseWriter, r *http.Request) {
	/*
	 * YOUR CODE HERE
	 *
	 * Try running `go test`.  Add more test as you code in `handle_test.go`.
	 */
	fmt.Print("Server: recieved message!\n") // printed on server
	fmt.Fprint(w,"Hello, Little World!\n") // printed on client
}

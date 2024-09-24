package function

import (
	"fmt"
	"net/http"
)

// Handle an HTTP Request.
func Handle(w http.ResponseWriter, r *http.Request) {
	fmt.Print("HELLO IN SERVER\n")
	fmt.Fprint(w, "HELLO IN CLIENT\n")
}

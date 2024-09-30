package function

import (
	"fmt"
	"net/http"
)

type MyFunction struct{}

func New() *MyFunction {
	return &MyFunction{}
}

func (f *MyFunction) Handle(res http.ResponseWriter, req *http.Request) {
	fmt.Print("edited: hello there in server -- im an instance btw\n")
	fmt.Fprint(res, "edited: hello there in client, instanced btw\n")
}

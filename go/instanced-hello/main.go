package main

import (
	"fmt"
	"os"
	
	"knative.dev/func-go/http"
	f "function" // this is the actual function imported
)

func main() {
	fmt.Print("Starting main...\n")
	if err := http.Start(f.New()); err != nil{
		fmt.Fprint(os.Stderr,err.Error())
	}
}


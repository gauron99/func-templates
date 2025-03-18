package function

import (
	"net/http"
)

type Function struct {
	fileserver http.Handler
}

func New() *Function {
	return &Function{fileserver: http.FileServer(http.Dir("./dist"))}
}

func (f *Function) Handle(w http.ResponseWriter, r *http.Request) {
	f.fileserver.ServeHTTP(w, r)
}

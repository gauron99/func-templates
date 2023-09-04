# func-templates
Example Templates for Knative Functions

### tips
- dont edit func.yaml ?

Divide dirs for each language
```
go/
|
├ basic/
| ├ template/
| | └ <template to easily fetch>
| └ README.md
|   └ describes how to use, steps to manually (init, deploy -- easy)
└ advanced/
  ├ template/
  | └ <template to easily fetch>
  └ README.md
    └ describes advanced deploy (using build, --image, remote deploy w/ tekton)

- python
  - same as go
- node
  - same as go
- ...

```

### To Decide (TODO)
How to structure the templates?
- or maybe even have the 'basic' template in the parent dir so its templates/go/\<template\>"
without the 'basic' and keep only for 'advanced' (if advanced should be at all)
- have one basic template in each and explain the logic of deploys separately
- ditch 'basic' and 'advanced' and use specific names: go/hello-world, go/http, go/events with
templates where the parent folder go/ will contain some basic information

  #### 2 ways of deploying
  1. host builder -- long term goal using this as default
  2. mention the "old" and describe how to

### possible errors
```
Error: function may not implement both the static and instanced method signatures simultaneously
-> this happens when `func (f *F) Somename(){}` is defined as well as `func Handle(){}`
```
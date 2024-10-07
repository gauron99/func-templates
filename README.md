[![Invoke All Functions](https://github.com/gauron99/func-templates/actions/workflows/invoke-all.yaml/badge.svg)](https://github.com/gauron99/func-templates/actions/workflows/invoke-all.yaml)
[![License](https://img.shields.io/github/license/gauron99/func-templates)](https://github.com/gauron99/func-templates/blob/main/LICENSE)

# WELCOME To Knative Function Templates!

### Quick search

1. [Basic Information](#example-templates-for-knative-functions) TODO: first done
2. [Project Structure](#project-structure) TODO: first run
3. [How To Use](#how-to-use) TODO:
    1. [Prerequisites](#prerequisites) TODO:
    2. [Build a Function](#build-a-function) TODO:
    3. [Deploy a Function](#deploy-a-function) TODO:
4. [Extra Configuration]() TODO: Is this necessary?
5. [Tips & Tricks]() TODO: instanced/static methods?
6. [Q&A]() TODO: Probably get rid of this or tips section 
8. [Contact](#contact) TODO:

## Example Templates for Knative Functions
This repository showcases some use-cases for your Knative Functions!
It is a collection of function templates. The built-in templates
are either *http* or *cloudevents* and these are custom template overrides.

Templates in this repository include:
- The easiest Hello World (`hello`)
- Simple splash screen with **referenced .css file** and **.funcignore** (`splash`)
- Web blog with **serverside rendering** and **import statements** (`blog`)
- A "Contact Us" function with a **secret password** (`contact-us`)

See [project structure](#project-structure) to learn about repository and see how to [deploy](#deploy-a-function) your function.

## Project structure
 Directory structure is as follows: **root/[language]/[template]** where *root* is 
 the github repository itself, *language* is the programming language used and
 *template* is the name of the template. Function is created using templates via
 `--repository` flag when using `func create` command. More in [How-To-Use](#how-to-use) section.

 ```
github.com/gauron99/func-templates <--[root]
├── go <------------------------------[language]
│   └── hello <-----------------------[template]
│       └── function source files
│   └── splash-screen
│       └── ...   
├── node
│   └── hello
│   └── splash-screen
├── ...
```

## How To Use
You use these templates by creating your function via `--repository` flag which
means "create my function with this template". 

- Create a function in **golang** with **hello template** within the current (empty) directory

```
func create --repository=https://github.com/gauron99/func-templates --language go --template=hello
```

- TODO add more examples / explanations
### Prerequisites
- Download func
- Download docker
- Download local cluster runner (kind)
- Download cli commands for k8s (kubectl)
### Build a Function

#### Using the Host Builder
This is the prefered way

#### Using Alternative Builders
This is the old way (pack/s2i)

### Deploy a Function

#### Local

#### Remote

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
# Contact
You can contact us on CNCF Slack [knative-functions](https://cloud-native.slack.com/archives/C04LKEZUXEE) channel
### possible errors
```
Error: function may not implement both the static and instanced method signatures simultaneously
-> this happens when `func (f *F) Somename(){}` is defined as well as `func Handle(){}`
```

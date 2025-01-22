[![Invoke All Functions](https://github.com/gauron99/func-templates/actions/workflows/invoke-all.yaml/badge.svg)](https://github.com/gauron99/func-templates/actions/workflows/invoke-all.yaml)
[![License](https://img.shields.io/github/license/gauron99/func-templates)](https://github.com/gauron99/func-templates/blob/main/LICENSE)

# WELCOME To Knative Function Templates!

## Quick search

1. [Basic Information](#templates-for-knative-functions) TODO: first done
2. [Prerequisites](#prerequisites) TODO: link to Luke's separate readme
3. [How To Use](#how-to-use) TODO:
    1. [Prerequisites](#prerequisites) TODO:
    2. [Build a Function](#build-a-function) TODO:
    3. [Deploy a Function](#deploy-a-function) TODO:
4. [Extra Configuration]() TODO: Is this necessary?
5. [Tips & Tricks]() TODO: instanced/static methods?
6. [Q&A]() TODO: Probably get rid of this or tips section 
7. [Contact](#contact) TODO:

## Templates for Knative Functions
This repository showcases some use-cases for your Knative Functions!
It is a collection of function templates. The built-in templates
are either *http* or *cloudevents* and these are custom template overrides.

Templates in this repository include:
- The easiest Hello World (`hello`)
- Simple splash screen with **referenced .css file** and **.funcignore** (`splash`)
- Web blog with **serverside rendering** and **import statements** (`blog`)
- A "Contact Us" function with a **secret password** (`contact-us`)

See [templates structure](#templates-structure) to learn about repository and
see how to [deploy](#deploy-a-function) your function.

## Prerequisites
In order to use Functions, you will need a few things:

### Download the `func` binary
You can clone our [GitHub repository](https://github.com/knative/func/) and 
build your binary from the source or download it straight from the
[release pages](https://github.com/knative/func/releases) under *Assets*.

Alternatively, for your convenience, see if your OS and architecture can be
found in the list below for an easy copy&paste and download our latest version
`knative-v1.16.1`.

### Linux

#### amd64
```bash
curl -L -o /usr/local/bin/func https://github.com/knative/func/releases/download/knative-v1.16.1/func_linux_amd64
```

#### arm64
```bash
curl -L -o /usr/local/bin/func https://github.com/knative/func/releases/download/knative-v1.16.1/func_linux_arm64
```

### Windows

#### PowerShell
```powershell
Invoke-WebReqest -Uri "https://github.com/knative/func/releases/download/knative-v1.16.1/func_windows_amd64.exe" -OutFile <"C:\path\to\your\destination\func.exe">
```
alternatively if `curl` is pre-installed
```powershell
curl -L -o <C:\path\to\your\destination\func.exe> "https://github.com/knative/func/releases/download/knative-v1.16.1/func_windows_amd64.exe" 
```
*NOTE: You need to change the part in <> to your desired destination*
*(don't include the "<>" symbols)*
### Mac (darwin OS)

#### amd64

```sh
curl -L -o /usr/local/bin/func "https://github.com/knative/func/releases/download/knative-v1.16.1/func_darwin_amd64"
```

#### arm64

```sh
curl -L -o /usr/local/bin/func "https://github.com/knative/func/releases/download/knative-v1.16.1/func_darwin_arm64"
```

*NOTE: After downloading on MacOS and Linux, you might need to make the file
executable*

```sh
chmod +x /usr/local/bin/func
```

### Get a containerization technology
These are some open-source examples of what you can use with Functions. You will
need some tools to atleast build and push your images. This list is not exhaustive.

[Buildah](https://github.com/containers/buildah/blob/main/install.md) - CLI tool
to build your images.

[Podman](https://podman.io/docs/installation#installing-on-linux) - complementary
to Buildah. Helps you manage and modify your images. Uses Buildah's golang API.
Can be installed independently. (*You can get this as a standalone tool*)

[Docker Engine](https://docs.docker.com/engine/install/) - Helps you build and 
containerize your applications. (*You can get this as a standalone tool*)

#### Download local cluster runner (kind)
Please refer to kind
[installation page](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
or download any other runner that you like.
#### Download cli commands for k8s (kubectl)
In order to interact with the objects in k8s, its recommended to get
[kubectl](https://kubernetes.io/docs/tasks/tools/).

## How To Use
You use these templates by creating your function via `--repository` flag which
means "create my function with this template".

Create your functions directory and `cd` into it

```
mkdir -p ~/testing/myfunc && cd ~/testing/myfunc
```

- Create a function in **golang** with **hello template** within the new (current and empty) directory

```
func create --repository=https://github.com/gauron99/func-templates --language go --template=hello
```

- TODO add more examples / explanations
### Build a Function

#### Using the Host Builder
This is the prefered way

#### Using Alternative Builders
This is the old way (pack/s2i)

### Deploy a Function

#### Local

#### Remote

## Templates structure
 Directory structure is as follows: **root/[language]/[template]** where *root* is 
 the github repository itself, *language* is the programming language used and
 *template* is the name of the template. Function is created using templates via
 `--repository` flag when using `func create` command. More in [How-To-Use](#how-to-use) section.

```
github.com/gauron99/func-templates <--[root]
├── go <------------------------------[language]
│   ├── hello <-----------------------[template]
│   │   └── <function source files>
│   └── splash-screen
│       └── ...   
├── node
│   ├── hello
│   └── splash-screen
├── ...
```
# Contact
You can contact us on CNCF Slack [knative-functions](https://cloud-native.slack.com/archives/C04LKEZUXEE) channel
### F&Q
```
Error: function may not implement both the static and instanced method signatures simultaneously
-> this happens when `func (f *F) Somename(){}` is defined as well as `func Handle(){}`
```

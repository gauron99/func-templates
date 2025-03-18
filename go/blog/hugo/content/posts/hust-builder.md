---
title: "The new and improved Host Builder"
description: Introduction of the Host Builder
date: 2025-03-13
keywords: ["gohugo", "hugo", "go", "blog"]
tags: ["hugo", "themes"]
summary: This post explains what the new Host Builder is and why its our new default
---

## The Host Builder
We have introduced the Host Builder (currently in active developement) some months
ago and its already been available behind a flag *FUNC_ENABLE_HOST_BUILDER* which
needs to be set to truthy value in order to use it.

# Why use it?
It's way faster to build your Functions!. Func will package your Functions
directory as an archive in a specific way into an image ready to be 'run'
locally on your machine, within seconds!

## Building example

{{< details summary="with time" >}}
Example of a go Function build using the Host Builder
```
❯ FUNC_ENABLE_HOST_BUILDER=1 time func build --builder=host
Building function image
   f.linux.amd64
   f.linux.arm64
   f.linux.arm.v7
🙌 Function built: quay.io/dfridric/random:latest
1.64user 0.67system 0:01.52elapsed
```
{{< /details >}}

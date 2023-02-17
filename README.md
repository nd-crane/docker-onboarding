# docker-onboarding
This is a quick introductory guide for getting started with Docker for the TAI project.

## What is Docker

[This](https://youtu.be/eGz9DS-aIeY) is the the best simple video explination of Docker, if you watch the first 6 minutes.
Docker serves also as the foundation for moving onto [Platform One](https://p1.dso.mil).

## Downloading

The best Tutorial for Docker is from Docker itself. First download the [desktop version](https://www.docker.com/products/docker-desktop/). 

## Get Started Tutorial
Next is to follow the [getting started](https://docs.docker.com/get-started/) tutorial. Follow this addtional information when doing the tutorial:

#### Dockerfiles
In Part 2, the tutorial does not go very in depth with how to actually create a Dockerfile (very important). Follow this [link](https://docs.docker.com/build/building/packaging/) on creating a Dockerfile, the foundation of your image.

#### Chip Architecture and Errors
You will run into some errors in the tutorial, depending on how you build your images and containers. Apple Silicon arm64 containers will not run on amd64. The first such error that shows up in this tutorial is when you upload to the 'Play with Docker' website, which runs a server on amd64_86. In the future, when you are building containers, many will fail as their dependecies will require the installation of amd64 dependecies without support for arm64.

The way to bypass is through emulation, which is packaged in within Docker software. The drawback to this method is that it drastically reduces the computational speed on the host machine (your Mac).

So following the tutorial, one method to change the architecture is through [buildx](https://docs.docker.com/build/building/multi-platform/). This link is a overview of multi-platform images and how to use them.

The command in the tutorial would look like:

```
docker buildx build --platform=linux/amd64 -t getting-started .
```

Then you can upload the image to 'Play with Docker'.

An alternative is to just use the regular Docker commands without buildx (not as many capabilities of buildx though), in which you would just flag it as such:
```
docker build --platform linux/amd64 -t getting-started .
docker run --platform linux/amd64 getting-started

```

#### Virtual Box
You may run into an error when using volumes on Part 5 of the tutorial. This error comes up when the container starts and stops imedialty with a (126) Error. To solve this you need to install [virtual box](https://www.virtualbox.org). There is no official build for Apple Silicone yet, so download the developer's version.

## Python 
Once you have completed the tutorial to understand the basics of Docker and development, move to the [next tutorial](https://docs.docker.com/language/python/) which is specific to our most commonly used language for TAI, Python.




# docker-onboarding
This is a quick introductory guide for getting started with Docker for the TAI project.

## What is Docker

[This](https://youtu.be/eGz9DS-aIeY) is the the best simple video explination of Docker if you watch the first 6 minutes.
Docker serves also as the foundation for moving onto [Platform One](https://p1.dso.mil).

## Downloading

The best Tutorial for Docker is from Docker itself. First download the [desktop version](https://www.docker.com/products/docker-desktop/). 

### Get Started Tutorial
Next is to follow the [getting started](https://docs.docker.com/get-started/) tutorial. Follow this addtional information when doing the tutorial:

**Dockerfiles** In Part 2, the tutorial does not go very in depth with how to actually create a Dockerfile (very important). Follow this [link](https://docs.docker.com/build/building/packaging/) on creating a Dockerfile, the foundation of your image.

**Chip Architecture and Errors** You will run into some errors in the tutorial, depending on how you build your images and containers. Apple Silicon arm64 images will not run on amd64. The first such error that shows up in this tutorial is when you upload to the 'Play with Docker' website, which runs a server on amd64_86. 



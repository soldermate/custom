FROM mcr.microsoft.com/devcontainers/base:jammy
RUN apt-get update --fix-missing \
&& apt-get install python3


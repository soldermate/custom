FROM mcr.microsoft.com/devcontainers/base:jammy
RUN apt-get update \
&& apt-get install python3 postgresql-client

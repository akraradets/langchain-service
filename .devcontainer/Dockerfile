# Note: You can use any Debian/Ubuntu based image you want. 
FROM python:3.11.8-bookworm

ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install --upgrade pip
RUN pip install poetry==1.6.1
RUN pip install langchain-cli

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
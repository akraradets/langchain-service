# LangServe Template

`LangServe` is a framework for deploying a `chain` or an `agent` easily.
It is built with modularity in mind.
This modularity enables `LLM` developers to develop a `chain` and an `agent` as a separate package called `LangChain Template`.

- [LangServe Template](#langserve-template)
  - [How this is created?](#how-this-is-created)
  - [How to develop](#how-to-develop)
    - [Codespaces](#codespaces)
    - [Local Development](#local-development)
  - [How to deploy](#how-to-deploy)


## How this is created?

The project is created with `langchain-cli`

```sh
langchain app new .
```

The command will generate these files.
To install a virtual environment, you run

```sh
poetry install
```

To run the server

```sh
langchain serve
```

## How to develop

This repository is set as a template.
You can always create a new repository based on this one easily.
Or if you want to fork, feel free to do so.

After you spawn the `Dev Container` regardless of using `Codespaces` or `Local Dev Container`, it will install the extension and perform the `poetry install` right away.
The result of `poetry install` will create the `.venv` folder with nesseary Python package to run the project.
You can try to run 

```sh
langchain serve
``` 

to see if it works.

### Codespaces

The template is created with `GitHub Codespaces`.
We recommend you use `Codespaces` to develop.

### Local Development

We tested the `.devcontainer` on `Macbook Pro M3 pro` with `Docker Desktop` version 4.27.2. 
It seems to work just like `Codespaces`.

We have not yet tested this on `Windows` and `Linux/Ubuntu` but they should just work fine too.

## How to deploy

To deploy, we create a `docker-compose.yml` that will build the `Dockerfile`.
What you will need to provide is the `.env` file.

```sh
LANGCHAIN_TRACING_V2="false"
LANGCHAIN_API_KEY="<YOUR-API-KEY>"  # Update to your API key
LANGCHAIN_PROJECT="default"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
```

If you need more environment variables, you can add the `.env` file or create another one and append the list to `env_files` in `docker-compose.yml`

To build and run Docker.

```sh
docker compose up -d --build
```

This will spawn a Docker container that only runs the project (similar to the Production).
If this works fine, you should be safe to deploy.

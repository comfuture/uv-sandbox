# UV Sandbox

This repository is for usage test for the
[uv package manager](https://github.com/astral-sh/uv).

## Creating a new project

In the project working direcoty, run the following command:

```bash
> uv init
```

or you can specify the project name:

```bash
> uv init my_project
```

The `uv init` command will create a new project directory with `src` directory
in the root of the project directory. But no options are available for flat
project structure.

If you don't want to use the `src` directory, just delete it.

```bash
> mv src/* . && rm -rf src
```

## Virtualenv

Since uv has their own virtualenv system, you can create a new virtualenv

```bash
> uv venv
```

This will create a new directory `.venv` in the project directory.

If the virtualenv exists in the project directory, `uv` command will
automatically use the virtualenv.

Also, you can activate the virtualenv by running the following command:

```bash
> activate .venv/bin/activate
```

<!> If you are using pyenv and pyenv-virtualenv, please DO NOT create
`.python-version` file in the project directory. It will cause an error.

There are some shell scripts that helps you to activate the virtualenv when you
change the directory.

for example:
[zsh plugin](https://gist.github.com/kishannareshpal/342efc4a15e47ea5d338784d3e9a8d98)

## Installing packages

To add a new package, you can use the `uv add` command.

```bash
> uv add fastapi
> uv add uvicorn
> uv add --dev pytest
```

This will automatically update the `pyproject.toml` file.

The uv virtualenv does not includes the `pip` command. Instead, you can use the
`uv pip` command.

```bash
> uv pip install requests
> uv pip freeze > requirements.txt
```

## Other commands

Please refere to the
[uv documentation](https://docs.astral.sh/uv/getting-started/) for more
information.

# Data Science

## Prerequisite

- [uv](https://github.com/astral-sh/uv) - Python Package Installer and Resolver
- Select and install **Python version** - match `.python-version` file

## Setup

```bash
uv sync
```

## Editor/IDE

Match the python environment of editor, by selecting the right Python Kernel found in `.venv/bin/python`.

## Security

[Fickling](https://github.com/trailofbits/fickling) used to do basic security scan of `.p` files.

### Fickling

Use fickling's CLI to safety-check pickle files:

```sh
uv run fickling --check-safety -p <Pickle file/>
```

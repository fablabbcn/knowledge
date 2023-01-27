# Fab Lab Barcelona Knowledge Hub

[![SpellChecker](https://github.com/fablabbcn/knowledge/actions/workflows/spell-check.yml/badge.svg)](https://github.com/fablabbcn/knowledge/actions/workflows/spell-check.yml)

The project main documentation available at https://knowledge.fablabbcn.org

## Easy Usage

Look into the `docs` folder for the Markdown documents which you can edit or send a Pull Request.

Example, here is a list of our programs: https://github.com/fablabbcn/knowledge/tree/master/docs/programs

## Usage

We encourage you to simply edit Markdown files directly on Github.

If you want to build and test on your local machine, you need `python3`

### Install project locally

Python3 Virtual Env (recommended):

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

_In Windows if it fails use `pip install -r requirements.txt --user` instead._

### Edit

`mkdocs serve --livereload`

_In Windows if it fails use `python -m mkdocs serve --livereload` instead._

### Deploy

Deploy is done by default via Github Action. See `/.github/workflows/main.yml`. 

For custom installations you can use `mkdocs gh-deploy`.

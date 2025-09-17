# AIA Software Training

Learn the fundamentals of transform-based low-order modelling and analysis

## Developer Guide

### Dependencies

The required dependencies are defined in [`requirements.txt`](requirements.txt).
To install them inside a virtual environment using [venv](https://docs.python.org/3/library/venv.html), run:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Documentation

This repository uses [MkDocs](https://www.mkdocs.org) to generate a static documentation site for users.
The source files for the site can be found in the [`docs/`](docs) directory and site configuration in [`mkdocs.yml`](mkdocs.yml).
To serve the site locally, run:

```
mkdocs serve
```
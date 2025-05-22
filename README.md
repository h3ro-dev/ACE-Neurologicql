# ACE NeurologicQL

This repository contains a simple web-based assessment tool for exploring how adverse childhood experiences (ACEs) may impact neurological development. It includes minimal HTML pages, a CSS stylesheet, a basic test suite, and a `Dockerfile` for running in a container.

## Opening the HTML files

To view the static pages locally, open either `index.html` or `ace.html` in your web browser. No additional build step is required; simply double-click the files or serve them with any HTTP server if preferred.

## Running Tests

The repository uses Python's built-in `unittest` framework. Run the test suite from the repository root with:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

This command is the same one used in the provided Docker setup script.

## Building the Docker Image

A `Dockerfile` is provided for development and testing. Build and run the container with:

```bash
docker build -t repo-dev .
docker run --rm repo-dev ./codex/setup.sh
```

The setup script installs dependencies, starts background services required by the tests, and finally runs the Python tests.

## Research Objectives

This project is part of ongoing research into the relationship between specific childhood traumas and their effects on different brain regions. We are currently validating mappings of trauma types to affected brain areas to better understand potential clinical applications and further improve the assessment tool.


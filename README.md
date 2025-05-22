# AI Blackened Management System

This repository provides a minimal management system for processing
Adverse Childhood Experiences (ACEs) data. The implementation focuses
on a command line interface that can be extended with additional data.

## Features

- Interactive CLI for entering trauma experiences.
- Calculates impacted brain regions and systems.
- Summaries include potential superpowers and kryptonites.
- Code formatted using the **Black** style.

## Usage

Install requirements (if using virtual environment recommended):

```bash
pip install -r requirements.txt
```

Run the interactive assessment:

```bash
python -m ai_blackened_management.cli --interactive
```

The CLI will prompt for gender, trauma types, and details for each
occurrence, then output a simple report.

## Formatting

The project uses [Black](https://github.com/psf/black) for code
formatting. You can format the codebase by running:

```bash
black src
```

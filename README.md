<<<<<<< HEAD
# ACE-Neurologicql

This repository contains materials for the "Enhanced ACEs Impact on Brain Development Assessment" interface.

The repository is organized into communication **channels** to clarify the role of each component:

- `channels/system`: resources that represent the main interface or system components.
- `channels/user`: space for user-supplied data or resources.
- `channels/assistant`: a dedicated area for notes or resources used by the assistant (ChatGPT).

Place relevant files or documentation within these folders to keep each channel distinct. The existing `ace.html` file represents the system interface and remains at the project root.
=======
# ACE Neurologic Assessment

This repository hosts a simple HTML interface for exploring how adverse childhood experiences can affect brain development. The main assessment logic lives in `ace.html` with supporting styles in `style.css`.

## Accessibility Improvements

The following changes were made to improve accessibility in accordance with WCAG guidelines:

- Added `role="banner"` and `aria-label` attributes to structural elements for screen reader navigation.
- Provided alt text for the SVG logo via `role="img"` and a `<title>` element.
- Updated button elements with descriptive `aria-label`s.
- Adjusted colors to meet contrast requirements, including darker button and header backgrounds.
- Increased text contrast for notes and disabled states.

# ACE NeurologicQL

This repository contains a simple web-based assessment tool for exploring how adverse childhood experiences (ACEs) may impact neurological development. It includes minimal HTML pages, a CSS stylesheet, a basic test suite, and a `Dockerfile` for running in a container. The assessment JavaScript also provides `autoDelete` and `autoMerge` helper functions for managing trauma entries.

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

>>>>>>> origin/main

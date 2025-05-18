# Repository Guide

## Languages and Directories
- HTML: `ace.html`
- Python: tests under `tests/`

## Build and Test
- There is no build step.
- Run tests with `python -m unittest discover -s tests -p 'test_*.py' -v`.

## Docker
To build and test using Docker:

```bash
docker build -t repo-dev .
docker run --rm repo-dev ./codex/setup.sh
```

## Notes
All outbound-network MCP servers are intentionally excluded.

# ACE Neurologic Assessment

This repository hosts a simple HTML interface for exploring how adverse childhood experiences can affect brain development. The main assessment logic lives in `ace.html` with supporting styles in `style.css`.

## Accessibility Improvements

The following changes were made to improve accessibility in accordance with WCAG guidelines:

- Added `role="banner"` and `aria-label` attributes to structural elements for screen reader navigation.
- Provided alt text for the SVG logo via `role="img"` and a `<title>` element.
- Updated button elements with descriptive `aria-label`s.
- Adjusted colors to meet contrast requirements, including darker button and header backgrounds.
- Increased text contrast for notes and disabled states.


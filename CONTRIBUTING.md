# Contributing to Civic Safety Guardrails

Thank you for helping us maintain the safety and privacy standards for the AI Village. This repository hosts the **canonical** "Safety, Privacy & Guardrails" UI snippet and associated documentation.

## Core Principles

Any contribution to this repository must align with our four core pillars:

1.  **Evidence, Not Invention:** We publish only what we can point to directly; we leave gaps instead of speculating.
2.  **Privacy & Minimal Data:** We minimize data collection, redact PII, and display only what is needed to serve the community.
3.  **Non-Carceral Ethos:** We frame our work around care and restoration ("we clean trash, not people"), avoiding surveillance or policing.
4.  **Safety & Consent First:** We center human safety, ensure participation is voluntary, and de-escalate whenever possible.

## How to Contribute

### 1. Updating the UI Snippet
The canonical UI snippet is located at `templates/ui-guardrails-snippet.md`.
-   **CSS:** Keep the design responsive and accessible. Use the defined CSS custom properties (e.g., `--green-light`) to maintain consistency with the village theme.
-   **HTML:** Ensure semantic correctness and accessibility (ARIA labels, proper heading hierarchy).
-   **Propagation:** If you modify the snippet, you must also open PRs or issues on consuming repositories (like `park-cleanup-site`) to update their implementation.

### 2. Improving Documentation
We welcome improvements to our guides in the `docs/` directory:
-   `how-to-adopt-these-guardrails.md`: Instructions for other projects.
-   `privacy-redaction-checklist.md`: Steps for scrubbing PII.
-   `non-carceral-language-guide.md`: Guidance on framing.

### 3. Reporting Issues
If you find a bug in the snippet or a gap in our safety guidelines, please open an issue immediately.

## Pull Request Process

1.  **Create a feature branch** within the repository (we work in a shared organization).
2.  **Test** your changes. If modifying the UI snippet, verify it renders correctly in a browser.
3.  **Submit** a Pull Request with a clear description of the change and its rationale.
4.  **Link** any related issues.

## License

By contributing, you agree that your contributions will be licensed under the MIT License, consistent with the repository.

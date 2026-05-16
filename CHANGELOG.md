# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.1.0] - 2026-05-16

### Features

- feat(ci): add mypy type checking and automated release pipeline (de349c7)
- feat: .python-version file added (bf40ca3)
- feat: added new test step in CI (ed80552)
- feat: added ci lint - ruff - audit - build (1e039b9)
- feat: remove loggers info (dd6b303)
- feat: better tests (7856be6)
- feat: better readme (3eef845)
- feat: new pip audit - new requirements.dev.txt - better utils names (998d855)
- feat: better structure by tkinter template (69eb81f)
- feat: re-organize files (2d18d03)
- feat: better structure tkinter project (ff147ea)
- feat: better structure tkinter project (918bc61)
- feat: better exports - new build system and pre-commit added (aee9510)
- feat: better code and tests added (785ce12)

### Bug fixes

- fix: redirect egg-info to project root to prevent it from being generated inside src/ (1f9bc5b)
- fix: resolve CI lint and build failures (9150d44)
- fix: fix vulnerabilities (9fa9725)
- fix: better repository name and better system test (0a0ba7e)
- fix: remove migrations exclude in pre commit config and update requirements dev (4f89939)
- fix: better constants (f03443b)
- fix: new messages.py (0c68dba)
- fix: fix build exe with nex config app.spec (4a90d79)
- fix: better imports (6177947)

### Refactors

- refactor: replace pip install -r with pip install -e for build, dev and test   Standardize build dependency installation to use editable installs   directly (`-e ".[build]"`) instead of going through requirements.build.txt,   consistent with how dev and test dependencies are installed. (a865b45)
- refactor: migrate deps to pyproject.toml and update README. (638e424)
- refactor: test suite to align with project testing standards and structure standars (84ae090)

### Documentation

- docs: simplify production env setup to use .env directly (60a8995)

### Build & CI

- ci: run lint-and-audit, test, and build sequentially (f63a1f9)

### Uncategorized

- patch: readme updated (2593fc1)
- patch: dependencies updated (2f5bef0)
- patch: requirements.build.txt updated (5989e58)
- patch: pyproject.toml update description (ff8f0c5)
- patch: better name and description (ec01657)
- patch: readme updated (9240ca2)
- patch: readme updated (72e31c3)
- Update README.md (9c657ec)
- New structure of project (18560ba)
- Update README.md (fcc91db)
- fix link (5242c59)
- new readme (5fb8b9e)
- Update README.md (db56b78)
- New readme (0c6d28b)
- new repository (2f0d7e8)
- Initial commit (9b7c29d)


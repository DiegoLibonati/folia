# Folia

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Folia** is a lightweight, desktop text editor built with Python and Tkinter, designed to provide a clean and distraction-free writing experience directly on your operating system — no browser, no cloud, no dependencies beyond a Python runtime.

At its core, Folia works like a modern notepad: you can create new text documents from scratch, open existing `.txt` files from your filesystem, edit their content freely, and save them back — either overwriting the original file or saving to a new location. The editor supports standard text operations and gives you a familiar, native-feeling interface that stays out of your way.

Beyond basic editing, Folia lets you personalize the reading and writing experience through its built-in font configuration panel. You can change the font family and adjust the font size to whatever feels most comfortable, making it equally suitable for quick note-taking or longer writing sessions.

The application is architected with a clear separation between UI, services, and configuration, making it easy to understand and extend. It uses a global error handling system that surfaces user-facing issues as dialog messages rather than silent failures or crashes. Environment-based configuration (`development`, `production`, `testing`) allows the app to behave differently depending on the context it runs in, which is particularly useful during development and automated testing.

Folia can also be packaged into a fully standalone executable using PyInstaller, meaning end users can run it without having Python installed at all — just a single binary or `.exe` file.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

Dependencies are declared in `pyproject.toml`. The `requirements*.txt` files are thin wrappers that delegate to it.

#### Runtime (`[project.dependencies]`)

```
python-dotenv==1.2.2
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
mypy==1.13.0
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==9.0.3
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build (`[project.optional-dependencies]` build)

```
pyinstaller==6.16.0
```

## Getting Started

With the dependencies listed above in mind, follow these steps to run the project locally.

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e ".[dev,test]"`

   Alternatively, you can install each group separately:
   - `pip install -e "."` — runtime only
   - `pip install -e ".[dev]"` — adds dev tools
   - `pip install -e ".[test]"` — adds test tools

6. Copy `.env.example.dev` to `.env` so the app can load its environment configuration
7. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The `.env` file you copied during setup is read at startup. The following keys control runtime behavior:

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Testing

With the project running locally, you can verify everything works by executing the test suite.

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e ".[test]"`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

Before shipping a build, check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e ".[dev]"`
4. Execute: `pip-audit`

## Build

Once tests pass and dependencies are clean, you can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

> **Important:** The build bundles the repo-level `.env` into the executable. For production builds,
> set production values directly in `.env` — never commit real secrets to the repo.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Continuous Integration

The repository ships with a **GitHub Actions** pipeline defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). It runs automatically on every `push` and `pull_request` targeting the `main` branch. On `push` to `main`, the same workflow continues with three additional jobs that produce an automated release.

### Pipeline overview

```
                      ┌─── PR or push to main ───┐
                      ▼                          ▼
┌──────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│   lint-and-audit     │─▶│       test       │─▶│      build       │
│ ruff · mypy · audit  │  │ pytest (headless)│  │ pyinstaller (lnx)│
└──────────────────────┘  └──────────────────┘  └──────────────────┘
                                                          │
                                       (only on push to main, sequentially)
                                                          ▼
                                                ┌──────────────────────┐
                                                │   prepare-release    │
                                                │ bump · changelog · tag│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │  build-windows-exe   │
                                                │ pyinstaller (windows)│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │   publish-release    │
                                                │ GitHub Release + .exe│
                                                └──────────────────────┘
```

### Validation jobs (run on every PR and push)

1. **`lint-and-audit`** — `ruff check`, `ruff format --check`, `mypy --config-file=pyproject.toml .`, `pip-audit --skip-editable`.
2. **`test`** — installs `python3-tk` + `xvfb` on Ubuntu and runs `xvfb-run python -m pytest --tb=short` headlessly.
3. **`build`** — smoke test that `pyinstaller app.spec` produces a binary on Linux (copies `.env.example.prod` to `.env` beforehand and verifies that `dist/app` exists).

### Release jobs (only on push to `main`)

4. **`prepare-release`** — inspects the commits since the latest tag, decides the next SemVer version using [Conventional Commits](#conventional-commits-required-for-releases), generates the changelog section, updates `CHANGELOG.md` and `pyproject.toml`, then commits, tags and pushes back to `main`. Skipped automatically when the head commit is the bot's own `chore(release): vX.Y.Z` commit, to avoid loops.
5. **`build-windows-exe`** — checks out the freshly created tag on a `windows-latest` runner, runs `pyinstaller app.spec`, and renames the artifact to `folia-vX.Y.Z-windows.exe`.
6. **`publish-release`** — creates the GitHub Release for the new tag, attaches the Windows `.exe`, and uses the generated changelog section as the release notes.

### Conventional Commits (required for releases)

Commits merged into `main` must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so the pipeline can compute the next version and group the changelog entries.

| Commit prefix | Version bump | Example |
|---|---|---|
| `feat:` / `feat(scope):` | **MINOR** | `feat(ui): add dark mode toggle` |
| `fix:` / `fix(scope):` | **PATCH** | `fix: prevent crash on empty file` |
| `perf:`, `refactor:`, `docs:`, `build:`, `ci:`, `chore:`, `style:`, `test:` | **PATCH** | `refactor: extract font config form` |
| `feat!:` / `fix!:` or `BREAKING CHANGE:` in the body | **MAJOR** | `feat!: rewrite config loader` |

When a push contains multiple commits, the highest applicable bump wins (a single `feat:` among many `fix:` triggers a MINOR bump). If you squash-merge PRs, configure the repo to use the PR title as the squash commit message and write the **PR title** following the convention.

### Skipping a release

If you need to push a change to `main` without producing a release (e.g. tweaking job names in the workflow, fixing a typo in the README), append `[skip release]` to the commit message. The validation jobs (lint, test, build) still run; only `prepare-release`, `build-windows-exe` and `publish-release` are skipped.

```bash
git commit -m "ci: rename build job for clarity [skip release]"
```

To skip **everything** including validation, use GitHub's standard `[skip ci]` marker instead.

### Where the build outputs live

| Output | Location |
|---|---|
| Validation logs (lint, tests) | **Actions** tab on GitHub |
| Linux smoke-build binary | Ephemeral, inside the runner |
| Windows `.exe` per version | **Releases** page (sidebar of the repo) |
| Version history & notes | [`CHANGELOG.md`](CHANGELOG.md) + Releases page |

> **Note:** GitHub's **Packages** section is for package registries (npm, PyPI, Docker, etc.) and does not host PyInstaller executables. Standalone binaries always live under **Releases**.

### Repository setup required for releases

For the release jobs to push tags and commits back to `main`, the repository needs:

1. **Settings → Actions → General → Workflow permissions**: set to *Read and write permissions*.
2. **Branch protection on `main`**: if enabled, allow the `github-actions[bot]` to bypass the PR requirement, or disable the protection for the bot. Otherwise `prepare-release` will fail when pushing the version bump.

### Running the same checks locally

```bash
# lint-and-audit
ruff check .
ruff format --check .
mypy --config-file=pyproject.toml .
pip-audit --skip-editable

# test
pytest --tb=short

# build
pyinstaller app.spec
```

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/folia`](https://www.diegolibonati.com.ar/#/project/folia)

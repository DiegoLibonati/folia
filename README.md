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

#### Requirements.txt

```
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Getting Started

With the dependencies listed above in mind, follow these steps to run the project locally.

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`

   Alternatively, if you installed the project as an editable package (`pip install -e ".[dev,test]"`), steps 5–7 can be replaced by that single command.

8. Copy `.env.example.dev` to `.env` so the app can load its environment configuration
9. Use `python app.py` or `python -m src` to execute the program

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
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Security Audit

Before shipping a build, check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Build

Once tests pass and dependencies are clean, you can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

> **Important:** The build bundles the repo-level `.env` file into the executable. For production builds,
> never put real secrets in the repo-level `.env`. Create a separate `.env.prod`, copy it to `.env` right
> before running PyInstaller, then remove it from the repo root afterwards.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/folia`](https://www.diegolibonati.com.ar/#/project/folia)

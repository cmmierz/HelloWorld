# HelloWorld

A simple project to demonstrate the classic "Hello, World!" example.

## Getting Started

1. Clone the repository.
2. Run the main program file.

## Features

- Prints "Hello, World!" to the console.

## License

This project is licensed under the MIT License.

Recreate the virtual environment (only if you don't already have the .venv folder):
'python -m venv .venv'
This will make a '.venv' folder in your HyporheicFloPy directory.

To access the virtual environment in command prompt use:
'.venv\scripts\activate'

To get the latest packages in your virtual environment:
'pip install -r requirements.txt'

To install packages to your virtual environment

activate the virtual environment (if it's not already active)
use 'pip install [package name]'
to uninstall use 'pip uninstall [packagename]'
Before updating requirements.txt, always pull the latest changes:
'git pull origin main'
'pip install -r requirements.txt'

If you add packages to your virtual environment, you'll need to update requirements.txt:
'pip freeze > requirements.txt'

You can push changes with source control. Always use a concise commit message to describe the change.
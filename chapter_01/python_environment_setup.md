# Python Development Environment Setup for Windows

## System Requirements
- Windows 10/11 64-bit
- Minimum 4GB RAM (8GB recommended)
- 10GB free disk space
- Internet connection for package installation

## Installation Steps

### 1. Python Installation via Scoop

```powershell
# Add required buckets
scoop bucket add extras
scoop bucket add versions

# Install Python
scoop install python

# Verify installation
python --version  # Should show Python 3.9+
pip --version

### 2. Git Configuration

git config --global user.name "Your Name"
git config --global user.email "your.email@berkeley.edu"
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global credential.helper manager

### 3. VS Code Setup

1.Install VS Code from Microsoft Store or scoop

2.Install essential extensions:

    Python (ms-python.python)

    Pylance (ms-python.vscode-pylance)

    Python Docstring Generator

    GitLens

    Code Runner

    Prettier

### 4. Project Setup

# Clone or create project directory
cd Documents
mkdir python-crash-course-ucb
cd python-crash-course-ucb

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

### 5. Verification

python chapter_01/hello_world/advanced_hello.py
pytest tests/test_chapter_01.py -v

Troubleshooting

Virtual Environment Issues

If activation fails, run:

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

VS Code Issues

If Python interpreter not detected:

    1.Press Ctrl+Shift+P

    2.Type "Python: Select Interpreter"

    3.Choose .venv\Scripts\python.exe

Resources

    1.Python Documentation

    2.VS Code Python Tutorial

    3.Git Documentation
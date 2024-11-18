# Silver Fund Signal Research
Unified research repository for BYU Silver Fund's quant team.

## Getting Started
We are going to use a python package and project manager called uv. If you have not used it before, you can read the docs
[here](https://docs.astral.sh/uv/). This is going to make it easier for everyone to be on the same page and have a universal
coding environment.

### Step 1: Install `uv` from your system terminal (not in vscode) if you have not already installed it.

#### MacOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Other Methods of Download including PyPy and Homebrew
[Here](https://docs.astral.sh/uv/getting-started/installation/)

### Step 2: Create virtual environment and install dependencies
We are going to use 'uv sync' to manage our venv and its dependencies. If there is not already a .venv in the project, which
is probably the case, then it will create one for you. Within the venv, it will download everything in pyproject.toml.
What's probably most important to you in this file are the dependencies that are installed.

```bash
uv sync
```

After creating your venv, it probably won't be running. If this is the case, run the following:
```bash
source .venv/bin/activate # MacOS/Linux
```
```bash
.venv/Scripts/activate # Windows
```
You'll now see that the venv you created is activated and running by going to terminal and seeing (sf-signal-research).

### Add pre-commit hook
```bash
pre-commit install
```
That's it! You're all good to go!

## Miscellaneous

### Cleaning code
```bash
pre-commit run --all-files
```

### Troubleshooting
If your imports are still giving you trouble. It means one of the following things:

#### 1. Your interpreter is messed up
##### Go to:
###### PyCharm
Windows: File->Settings->Project->Python Interpreter

Mac: PyCharm->Settings->Project->Python Interpreter
###### VSCode
Kernel->Python Environments->.venv

#### 2. The dependency isn't in pyproject.toml
Add it to the dependencies list and run 'uv sync' or add it at the top of file. See example project.

# Development Setup Instruction

### Requirements
`python` version 3.7 or higher. Also make sure `pip`, `venv`, and `distutils` are installed.

### Step 1: Create virtual enviroment
Run `python3 -m venv .venv`.
Then if you are on Windows, run `.\.venv\Scripts\activate.bat`. Otherwise, run `source .venv/bin/activate`.
You are now inside your virtual environment.

### Step 2: Install required packages
Run `pip install wheel` to install wheel, which is needed for the installation process of a few packages in
`requirements.txt`. Then run `pip install -r requirements.txt` to install all required packages. You would then
also want to run `pre-commit install`. `pre-commit` will be run eveytime you commit your code to make sure
the code is clean.

### Step 3: Local configuration
Add a file named `local_settings.py` to `config` folder. In this file, you can override the configurations and 
credentials locally.

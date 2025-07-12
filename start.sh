#!/bin/bash

# Step 0: Ensure system dependencies are installed
# Install gfortran (used for compiling scientific Python packages)
sudo apt-get update && sudo apt-get install -y gfortran

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "venv_agent_lab" ]; then
  python -m venv venv_agent_lab
fi

# Step 2: Use venv's pip to install requirements with pre-built wheels
venv_agent_lab/bin/pip install --upgrade pip setuptools wheel
venv_agent_lab/bin/pip install --only-binary=:all: -r requirements.txt

# Step 3: Run Streamlit
venv_agent_lab/bin/streamlit run langchain.py

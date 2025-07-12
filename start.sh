#!/bin/bash

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "venv_agent_lab" ]; then
  python3.10 -m venv venv_agent_lab
fi

# Step 2: Use venv's pip to install requirements with pre-built wheels
venv_agent_lab/bin/pip install --upgrade pip setuptools wheel
venv_agent_lab/bin/pip install --only-binary=:all: -r requirements.txt

# Step 3: Run Streamlit
venv_agent_lab/bin/streamlit run langchain.py
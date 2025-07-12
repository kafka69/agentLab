#!/bin/bash

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "venv_agent_lab" ]; then
  python3.10 -m venv venv_agent_lab
fi

# Step 2: Use venv's pip to install requirements (no need to activate)
pip install --upgrade setuptools wheel
venv_agent_lab/bin/pip install -r requirements.txt

# Step 3: Run Streamlit globally (outside the venv)
streamlit run langchain.py

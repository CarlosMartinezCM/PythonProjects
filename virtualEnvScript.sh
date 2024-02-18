#!/bin/bash
# To activate the Virtual Enviroment I had to use the full file path to the Virtual Enviroment

# Checking if the Virutal Environment exist.
if [ -d "env" ]; then
    # If Virutal Environment exist, activate the environment 
    # shellcheck disable=SC1091
    source C:/Users/CAEC/Projects/py/PythonProjects/env/Scripts/activate # Use the appropriate slashes for OS
    echo "Virtual environment activated."
else
    # Ask user if thery would like to create the virtual environment
    read -r -p "Virtual environment directory 'env' does not exist. Would you like to create one? (y/n): " choice
    if [ "$choice" == "y" ]; then
        # If yes, create the environment
        python -m venv env
        echo "Virtual environment 'env' was created successfully."
        # shellcheck disable=SC1091
        source C:/Users/CAEC/Projects/py/PythonProjects/env/Scripts/activate # Use the appropriate slashes for OS
        echo "Virtual environment activated."
    else 
        echo "Virtual environment creation/activation was aborted."
    fi
fi

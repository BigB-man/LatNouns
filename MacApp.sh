#!/bin/bash

# Function to check if Python is installed
check_python() {
    if command -v python3 &>/dev/null; then
        echo "Python is installed"
        return 0
    else
        echo "Python is not installed"
        return 1
    fi
}

# Function to prompt user to install Python
install_python_prompt() {
    echo "Python is required to run this script."
    echo "Please download and install Python 3.11.8 from the following link:"
    echo "https://www.python.org/ftp/python/3.11.8/python-3.11.8-macos11.pkg"
    echo "Once installed, please run this script again."
}

# Attempt to run the Python script
run_python_script() {
    if python3 LatinNounTester.py; then
        echo "Script ran successfully."
    else
        echo "Failed to run the script. Python may not be installed correctly."
        install_python_prompt
    fi
}

# Main script execution
check_python
if [ $? -eq 0 ]; then
    run_python_script
else
    install_python_prompt
fi

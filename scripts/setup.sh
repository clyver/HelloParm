#!/bin/bash

# installs homebrew if not aliased or installed
if hash brew 2>/dev/null; then
  echo "brew is already installed. Skipping."
else
  sudo ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
fi


# installs python if not aliased or installed
if hash python 2>/dev/null; then 
  echo "python is already installed. Skipping."
else
  brew install python 
fi

# installs pip if it does not exist
if hash pip 2>/dev/null; then
  echo "pip is already installed. Skipping."
else
  brew install pip
fi


# function to install pip packages
pip_installer() {
  if [[ -z $(pip freeze | grep "$1") ]]; then
    pip install "$1"
  else
    echo "$1 is already installed. Skipping."
  fi
}

# installs virtualenv
pip_installer virtualenv

# setups a virtualenv in the cwd
# FIXME should be able to use requirement.txt in this
if [[ ! -e .hackathon ]]; then
  virtualenv .hackathon
  . ./.hackathon/bin/activate
  pip_installer flask
  pip_installer flask-wtf
  pip_installer python-instagram
  deactivate
else
  echo "hackathon virtualenv already exists in the cwd. Skipping."
fi

echo "Script is done. Exiting."

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


# installs virtualenv
if [[ -z $(pip freeze | grep virtualenv) ]]; then
  pip install virtualenv
else
  echo "virtualenv is already installed. Skipping."
fi

# setups a virtualenv in the cwd
# should be able to use requirement.txt in this
if [[ ! -e hackathon ]]; then
  virtualenv hackathon
  hackathon/bin/pip install flask
  hackathon/bin/pip install flask-login
  hackathon/bin/pip install flask-openid
  hackathon/bin/pip install flask-mail
  hackathon/bin/pip install flask-sqlalchemy
  hackathon/bin/pip install sqlalchemy-migrate
  hackathon/bin/pip install flask-whooshalchemy
  hackathon/bin/pip install flask-wtf
  hackathon/bin/pip install flask-babel
  hackathon/bin/pip install guess_language
  hackathon/bin/pip install flipflop
  hackathon/bin/pip install coverage
else
  echo "hackathon virtualenv already exists in the cwd. Skipping."
fi

echo "Script is done. Exiting."

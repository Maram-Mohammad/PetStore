#!/bin/bash
set -e
# get parent dir
home="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/../ && pwd )"


# installs project dependencies
if [ "$CI" = true ]; then
    pip install -r $home/requirements-lock.txt
else
    # delete Python virtual environment and recreate it
    rm -rf $home/env
    # Do something under GNU/Linux platform
    virtualenv --python=python3.6 $home/env
    echo "export PYTHONPATH='$home'" >> $home/env/bin/activate
    # enter the venv and install dependencies
    source $home/env/bin/activate

    pip install -r $home/requirements.txt
    #freeze you environment to make sure the install is reproducable on CI
    # if you found pkg-resources==0.0.0 in requirements-lock.txt remove it --ubuntu bug--
    pip freeze > $home/requirements-lock.txt
fi

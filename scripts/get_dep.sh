#!/bin/bash
set -e
# get parent dir
home="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/../ && pwd )"
rm -rf $home/env
virtualenv --python=python3.6 $home/env
echo "export PYTHONPATH='$home'" >> $home/env/bin/activate
source $home/env/bin/activate
pip install -r $home/requirements.txt

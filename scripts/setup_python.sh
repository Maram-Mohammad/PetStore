
set -e 
# install requires : python - postrgres DB 

sudo apt install -y postgresql-client
#Install virtual environment 
sudo apt-get install -y python3-pip python3-dev
sudo pip3 install virtualenv 
sudo pip3 install pipenv
pip install --upgrade setuptools

export PYTHONPATH=$PWD
export FLASK_APP=app
export FLASK_DEBUG=1
source env/bin/activate
source env/Scripts/activate

flask db upgrade
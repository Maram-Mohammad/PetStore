export PYTHONPATH=$PWD
export FLASK_APP=app
export FLASK_DEBUG=1
source env/bin/activate
source env/Scripts/activate



echo "Starting docker compse"
docker-compose  -f docker-compose.yml up -d

echo "starting the dashboard flask app.."
python3 -m flask run --host=0.0.0.0


export PYTHONPATH=$PWD
export FLASK_APP=app
export FLASK_DEBUG=1
source env/bin/activate
source env/Scripts/activate

docker exec -it postgres_db dropdb -U adminuser petsdb.test
docker exec -it postgres_db createdb -O adminuser -U adminuser petsdb.test
python app/tests/user_api_test.py 

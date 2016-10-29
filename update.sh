git pull origin master
python3 manage.py collectstatic --noinput
python3 manage.py migrate
service gunicorn restart

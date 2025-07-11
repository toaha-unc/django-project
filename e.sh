source task_env/bin/activate;

python manage.py makemigrations;

python manage.py migrate;

python manage.py runserver;

python manage.py shell;
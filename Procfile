release: python manage.py makemigrations && python manage.py migrate
web: gunicorn laneys_loft.wsgi:application
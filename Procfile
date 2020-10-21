web: bin/start-nginx bin/start-pgbouncer-stunnel gunicorn -c gunicorn.conf djangoVue.wsgi:application
worker: bin/start-pgbouncer-stunnel python manage.py qcluster


release: sh -c 'cd coguard && python manage.py migrate'
web: sh -c 'cd coguard && gunicorn coguard.wsgi --log-file -'
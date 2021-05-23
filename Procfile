release: sh -c 'cd coguard && python manage.py migrate && python ./manage.py loaddata db.json'
web: sh -c 'cd coguard && gunicorn coguard.wsgi --log-file -'
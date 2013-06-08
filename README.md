## Djentrez site project

### 1. Install

1. install postgresql database, message-queue(redis here).
2. build a virtualenv and pip install -r requirements.txt

### 2. Configure on localhost

1. ./manage.py syncdb
2. ./manage.py migrate
3. ./manage.py runserver
4. check your browser in `http://127.0.0.1:8000`

### 3. Configure in the VPS

1. edit your virtualenv environment via `activate` file in the bin folder of virtualenv. put codes like `export SERVER='vps'` etc.
2. ./manage.py syncdb
3. ./manage.py migrate
4. ./manage.py run_gunicorn &
5. ./manage.py celeryd -B &

### 4. Settings in admin

1. add term in admin.
2. add crontab and peridictask in djcelery. remember put like `{'period': n}` (n is the day setting in your term)in your Keyword arguments.
3. check your site in the browser and wait until the worker finish your NCBI tracing.

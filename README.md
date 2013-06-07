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

1. edit your virtualenv environment via `activate` file in the bin folder of virtualenv. put codes like this

    export SERVER='vps'
    export EMAIL_ADDRESS='your@domain.com'
    ...

2. ./manage.py syncdb
3. ./manage.py migrate
4. ./manage.py run_gunicorn
5. check your site in the browser

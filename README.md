## Djentrez site project

### Install

1. install postgresql database, message-queue(redis here).
2. build a virtualenv and pip install -r requirements.txt

### Configure

1. edit your virtualenv environment via `activate` file in the bin folder of virtualenv. put codes like this

    export SERVER='vps'
    export EMAIL_ADDRESS='your@domain.com'
    ...

2. ./manage.py syncdb
3. ./manage.py migrate
4. ./manage.py run_gunicorn
5. check your site in the browser

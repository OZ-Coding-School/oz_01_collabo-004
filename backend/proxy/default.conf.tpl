server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }
#!/bin/sh

set -e


python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi:application
    location / {
        uwsgi_pass               ${APP_HOST}:${APP_PORT};
        include                  /etc/nginx/uwsgi_params;
        client_max_body_size     10M;
    }
}
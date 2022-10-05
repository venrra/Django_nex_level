#!/bin/bash
set -e

case "$1" in
    runserver)
        python /app/backend/manage.py runserver 0.0.0.0:8000
        ;;
    migrate)
        python /app/backend/manage.py migrate
        ;;
    collectstatic)
        python /app/backend/manage.py collectstatic --noinput
        ;;
    *)
        exec "$@"
esac
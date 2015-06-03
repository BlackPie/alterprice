#!/bin/bash
LOGS=/var/log/app/

if [ "$RUN_DEVSERVER" = "True" ]
then
    exec /project/bin/django runserver_plus 0.0.0.0:8000
else
    ( umask 0 && truncate -s0 $LOGS/* )
    tail --pid $$ -n0 -F $LOGS/* &
    exec /usr/local/bin/uwsgi --ini /project/src/uwsgi/${DJANGO_CONFIGURATION}.ini
fi
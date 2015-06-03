#!/bin/bash

if [ "$INSTANCE_TYPE" = "worker" ]
then
    /bin/start_celery.sh
else
    /bin/start_django.sh
fi
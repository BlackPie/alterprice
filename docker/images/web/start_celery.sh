#!/bin/bash

C_FORCE_ROOT="true" exec /project/bin/celery worker -B -A celeryconf -Q default -n default@%h
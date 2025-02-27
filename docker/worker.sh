#!/bin/bash

# unset http proxy which maybe set by docker daemon
export http_proxy=""; export https_proxy=""; export no_proxy=""; export HTTP_PROXY=""; export HTTPS_PROXY=""; export NO_PROXY=""


cd /app/server
PY=python3

function start_celery_worker(){
    while [ 1 -eq 1 ];do
      $PY -m celery -A app.celery_app worker --loglevel=info
    done
}

function start_celery_beat(){
    while [ 1 -eq 1 ];do
      $PY -m celery -A app.celery_app beat --loglevel=info
    done
}

start_celery_worker &
start_celery_beat &

wait;
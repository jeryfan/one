#!/bin/bash



# unset http proxy which maybe set by docker daemon
export http_proxy=""; export https_proxy=""; export no_proxy=""; export HTTP_PROXY=""; export HTTPS_PROXY=""; export NO_PROXY=""


cd /app/server
PY=python3
if [[ -z "$WS" || $WS -lt 1 ]]; then
  WS=1
fi

function start_admin(){
    while [ 1 -eq 1 ];do
      $PY -m uvicorn asgi:app --host 0.0.0.0 --port 8000 --proxy-headers --reload > /var/lib/logs/run_admin.log 2>&1
    done
}

function start_celery_worker(){
    while [ 1 -eq 1 ];do
      $PY -m celery -A app.celery_app worker --loglevel=info > /var/lib/logs/run_celery_worker.log 2>&1
    done
}

function start_celery_beat(){
    while [ 1 -eq 1 ];do
      $PY -m celery -A app.celery_app beat --loglevel=info > /var/lib/logs/run_celery_beat.log 2>&1
    done
}

start_admin &
start_celery_worker &
start_celery_beat &

wait;
#!/bin/bash

# unset http proxy which maybe set by docker daemon
export http_proxy=""; export https_proxy=""; export no_proxy=""; export HTTP_PROXY=""; export HTTPS_PROXY=""; export NO_PROXY=""


cd /app/server
PY=python3

function start_server(){
    while [ 1 -eq 1 ];do
      $PY -m uvicorn asgi:app --host 0.0.0.0 --port 8000 --proxy-headers --reload > /var/lib/logs/run_admin.log 2>&1
    done
}

start_server &

wait;
#!/usr/bin/env sh

. ./venv/bin/activate

exec gunicorn /societies/archim/webserver/archim/wgsi.py --bind unix:/societies/archim/sockets/django.sock


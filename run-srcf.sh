#!/usr/bin/env sh

. ./venv/bin/activate

exec gunicorn archim.wsgi --bind unix:/societies/archim/sockets/django.sock

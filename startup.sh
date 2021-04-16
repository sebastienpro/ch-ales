#!/usr/bin/env bash

set -e
exec gunicorn --bind 0.0.0.0:8000 wsgi:app --reload

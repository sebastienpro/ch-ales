#!/usr/bin/env bash

set -e
exec gunicorn --bind=unix:/tmp/gunicorn.sock wsgi:app --reload

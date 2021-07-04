#!/bin/bash

venv/bin/uwsgi --http-socket 0.0.0.0:8080 --master --module simpleEcho:app

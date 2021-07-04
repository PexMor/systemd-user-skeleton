#!/bin/bash

[ -d venv ] || virtualenv -ppython3 venv

venv/bin/pip install -r requirements.txt


#!/bin/bash

# make directory and navigate inside
mkdir iris-serverless-api
cd iris-serverless-api

# create virtual environment and activate it
python3.6 -m venv .
source bin/activate

# install our requirements
pip install -r requirements.txt

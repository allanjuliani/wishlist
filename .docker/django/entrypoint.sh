#! /bin/bash

cd /home/ubuntu/wishlist
pip install -r requirements.txt
./manage.py collectstatic
./manage.py migrate
.docker/django/gunicorn.conf

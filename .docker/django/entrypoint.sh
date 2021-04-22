#! /bin/bash

cd /home/ubuntu/wishlist

pip install -r requirements.txt

# su ubuntu --command "./manage.py collectstatic"
./manage.py collectstatic
./manage.py migrate

.docker/django/gunicorn.conf

FROM python:3.9-slim-buster

# ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get install default-libmysqlclient-dev build-essential -y

RUN python3 -m pip install --upgrade pip

RUN useradd -ms /bin/bash ubuntu

WORKDIR /home/ubuntu/wishlist

COPY . /home/ubuntu/wishlist

ENTRYPOINT ["/home/ubuntu/wishlist/.docker/django/entrypoint.sh"]

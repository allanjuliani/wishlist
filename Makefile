build:
	@cp .env.example .env
	@docker-compose build

rebuild:
	@docker-compose down --remove-orphans
	@docker-compose build --no-cache

up:
	@docker-compose up -d

down:
	@docker-compose down

install:
	@make build
	@make up

start:
	@docker start django_wishlist
	@docker start mysql_wishlist
	@docker start nginx_wishlist

stop:
	@docker stop django_wishlist
	@docker stop mysql_wishlist
	@docker stop nginx_wishlist

restart:
	@make stop
	@make start

wishlist-clean:
	@make down
	@docker image rm wishlist_django
	@docker volume rm wishlist_my-db

docker-clean:
	@make down
	@docker system prune -a
	@docker volume prune

tests:
	@docker exec -it django_wishlist python -m pytest -v apps --ds=wishlist.settings_test

cov:
	@docker exec -it django_wishlist python -m pytest -v apps --cov=apps --ds=wishlist.settings_test

createsuperuser:
	@docker exec -it django_wishlist python manage.py createsuperuser --noinput --settings=wishlist.settings_prod

createtoken:
	@docker exec -it django_wishlist python manage.py drf_create_token $(username)

shell-django:
	@docker exec -it django_wishlist /bin/bash

shell-mysql:
	@docker exec -it mysql_wishlist /bin/bash

shell-nginx:
	@docker exec -it nginx_wishlist /bin/bash

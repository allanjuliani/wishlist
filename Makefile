build:
	@docker-compose build

up:
	@docker-compose up -d

stop:
	@docker-compose down

rebuild:
	@docker-compose down --remove-orphans
	@docker-compose build --no-cache

remove:
	@docker-compose down --volumes --remove-orphans

wishlist-clean:
	@make stop
	@docker image rm django_wishlist

docker-clean:
	@make stop
	@docker system prune -a

createsuperuser:
	@docker exec -it django_wishlist python manage.py createsuperuser

createtoken:
	@docker exec -it django_wishlist python manage.py drf_create_token $(username)

shell-django:
	@docker exec -it django_wishlist /bin/bash

shell-mysql:
	@docker exec -it mysql_wishlist /bin/bash

shell-nginx:
	@docker exec -it nginx_wishlist /bin/bash

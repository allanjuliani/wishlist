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

clean:
	@docker image rm django_wishlist

createsuperuser:
	@docker exec -it django_wishlist python manage.py createsuperuser

shell-django:
	@docker exec -it django_wishlist /bin/bash

shell-mysql:
	@docker exec -it mysql_wishlist /bin/bash

shell-nginx:
	@docker exec -it nginx_wishlist /bin/bash
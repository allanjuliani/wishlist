PORT=8000
SITE=wishlist

start_br:
	@./manage.py runserver 0.0.0.0:$(PORT) --settings=$(SITE).settings_pt_br

start_en:
	@./manage.py runserver 0.0.0.0:$(PORT) --settings=$(SITE).settings

translate:
	@./manage.py makemessages -l pt_BR
	@./manage.py compilemessages -l pt_BR

migrate:
	@./manage.py makemigrations
	@./manage.py migrate

stop:
	@pkill -f $(PORT)

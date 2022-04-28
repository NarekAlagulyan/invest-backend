up:
	docker compose up

down:
	docker compsoe down

build:
	docker compose build

migrations:
	docker compose run --rm invest python3 manage.py makemigrations

migrate:
	docker compose run --rm invest python3 manage.py migrate

shell:
	docker compose run --rm invest python3 manage.py shell

bash:
	docker compose run --rm invest /bin/bash

collectstatic:
	docker compose run --rm invest python3 manage.py collectstatic

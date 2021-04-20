.PHONY: build reset down up cleardb mock

build:
	docker-compose build --parallel

test:
	docker-compose run --rm python-stock python main.py

up:
	docker-compose up -d saleor-api saleor-worker

down:
	docker-compose down --volumes

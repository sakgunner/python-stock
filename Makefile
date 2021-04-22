.PHONY: build reset down up

build:
	docker-compose build --parallel

test:
	docker-compose run --rm python-stock python main.py

down:
	docker-compose down --volumes

SHELL := /bin/bash

run:
	python app/main.py

deploy: 
	docker-compose build
	docker-compose up
	
down:
	docker-compose down

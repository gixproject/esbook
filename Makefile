help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build all or c=<name> containers in foreground
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) build $(c)

up: ## Start all or c=<name> containers in foreground
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up $(c) -d

test: ## Run tests
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec web invoke tests --path $(or $(c), '')

lint: ## Run linter for app folder
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec web flake8
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec web black /code/src/

logs: ## Show logs for all or c=<name> containers
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) logs --tail=$(or $(n), 100) -f $(c)

exec: ## Exec container
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec web bash

shell: ## Exec shell
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec web python manage.py shell

test-data:  ## Creates test data
	docker-compose exec web python manage.py test_data

start-server:  ## Starts the Nginx server
	docker-compose up -d --profile=server

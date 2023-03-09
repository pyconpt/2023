PROJECT_NAME=pycon_portugal_2023

# check form arm64 and apply override COMPOSE_FILE
# uname -m not used because we might be running a amd64 shell even in a arm-based mac
UNAME=$(shell uname -v)

COMPOSE_FILE=local.yml

export COMPOSE_FILE

.PHONY: help up build down start stop prune clear ps restore_db shell manage
default: up

## help	:	Print commands help.
help : Makefile
	@sed -n 's/^##//p' $<

## up	:	Start up containers.
up:
	@echo "Starting up containers for for $(PROJECT_NAME)..."
	# docker-compose pull
	# docker-compose build
	docker-compose up -d --remove-orphans

## build	:	Build python image.
build:
	@echo "Building python image for for $(PROJECT_NAME) using $(COMPOSE_FILE)..."
	docker-compose build

## down	:	Stop containers.
down: stop

## start	:	Start containers without updating.
start:
	@echo "Starting containers for $(PROJECT_NAME) from where you left off..."
	docker-compose start

## stop	:	Stop containers.
stop:
	@echo "Stopping containers for $(PROJECT_NAME)..."
	docker-compose stop

## prune	:	Remove containers and their volumes.
##		You can optionally pass an argument with the service name to prune single container
##		prune postgres	: Prune `mariadb` container and remove its volumes.
##		prune postgres redis	: Prune `postgres` and `redis` containers and remove their volumes.
prune:
	@echo "Removing containers for $(PROJECT_NAME)..."
	docker-compose down -v $(filter-out rm,$(filter-out $@,$(MAKECMDGOALS)))

## clear       :	Remove images, containers and their volumes. Also prunes docker
##		Use with caution
clear: prune
	@echo "Removing images for $(PROJECT_NAME)..."
	$(eval IMAGES=$(shell docker images -f 'reference=$(PROJECT_NAME)*' -q))
	@if [ -n "$(IMAGES)" ]; then docker rmi $(IMAGES); docker image prune -af; docker builder prune -af; fi

## ps	:	List running containers.
ps:
	docker ps --filter name='$(PROJECT_NAME)*'

# This hack allows for exec when an existing container is found, instead of run --rm
CONTAINER=django
RUN=exec
ENTRYPOINT='/entrypoint'
EXEC=$(shell docker-compose -f $(COMPOSE_FILE) $(RUN) $(CONTAINER) ls > /dev/null 2>&1; echo $$?)

ifeq ($(EXEC), 0)
	RUN=exec
	ENTRYPOINT='/entrypoint'
else
	RUN=run --rm
	ENTRYPOINT=
endif

## shell	:	Access `python` container via shell.
##		You can optionally pass an argument with a service name to open a shell on the specified container
shell:
	docker-compose $(RUN) $(CONTAINER) $(ENTRYPOINT) bash $(filter-out $@,$(MAKECMDGOALS))

## manage	:   python manage command
##		You can optionally pass an argument to manage
##		To use "--flag" arguments include them in quotation marks.
##		For example: make manage "makemessages --locale=pt"
manage:
	docker-compose $(RUN) $(CONTAINER) $(ENTRYPOINT) python manage.py $(filter-out $@,$(MAKECMDGOALS)) $(subst \,,$(MAKEFLAGS))


## restore_db	:	Restore database backup needs a database dump
##		Example: make restore_db xxx.sql.gz
##		Use with caution, not enough tests made yet
restore_db:
	$(eval DB_IMAGE_ID=$(shell docker ps --filter name='$(PROJECT_NAME).*postgres' --format "{{.ID}}"))
	docker cp $(filter-out $@,$(MAKECMDGOALS)) $(subst \,,$(MAKEFLAGS)) e94ed1a6622c:/backups
	docker-compose exec postgres restore $(filter-out $@,$(MAKECMDGOALS)) $(subst \,,$(MAKEFLAGS))


# https://stackoverflow.com/a/6273809/1826109
%:
	@:

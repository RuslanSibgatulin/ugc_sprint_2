## ----------------------------------------------------------------------
## The purpose of this Makefile is to manage UGC API project.
## ----------------------------------------------------------------------
compose_files=-f kafka-docker-compose.yml -f ugc-docker-compose.yml -f ch-docker-compose.yml -f elk-docker-compose.yml -f mongo-docker-compose.yml

help:     ## Show this help.
		@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

start:  ## Start project infrastructure.
		cd docker && DOCKER_BUILDKIT=1 docker-compose $(compose_files) up --build --force-recreate
stop:  ## Stop project.
		cd docker && docker-compose $(compose_files) down

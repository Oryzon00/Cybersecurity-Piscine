DOCKER_NAME	=	stockholm

all:	up

build:
		docker build -t ${DOCKER_NAME} .

up:		build
		docker run --name ${DOCKER_NAME} -d ${DOCKER_NAME}

stop:
		docker stop $(shell docker ps -qa)

purge:
		docker system prune -f

rm_img:
		docker image rm -f ${DOCKER_NAME}

re:
		make stop
		make rm_img
		make purge
		make up

exec:
		docker exec -it stockholm /bin/bash

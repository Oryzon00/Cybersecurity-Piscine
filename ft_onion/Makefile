DOCKER_NAME	=	ft_onion

all:	up

build:
		docker build -t ${DOCKER_NAME} .

up:		build
		docker run --name ft_onion -d -p 4243:22   ${DOCKER_NAME}
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

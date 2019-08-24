rebuild:
	docker rmi nameadvice || exit 0
	docker build --tag nameadvice .
deploy:
	docker-compose up -d
clean:
	docker stop nameadvice_1|xargs docker rm || exit 0
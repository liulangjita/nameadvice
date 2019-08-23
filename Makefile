rebuild:
	docker rmi nameadvice || exit 0
	docker build --tag nameadvice .
deploy:
	docker run -d --name nameadvice_1 nameadvice
clean:
	docker stop nameadvice_1|xargs docker rm || exit 0
DOCKER_IMAGE_NAME=dataesr/scientific-tagger
CURRENT_VERSION=$(shell cat project/__init__.py | grep -P '(\d\.?){3}' -o)

start:
	@echo Scientific Tagger starting...
	docker-compose up -d
	@echo Scientific Tagger started http://localhost:5004

release:
	echo "__version__ = '$(VERSION)'" > project/__init__.py
	git commit -am '[release] version $(VERSION)'
	git tag $(VERSION)
	@echo If everything is OK, you can push with tags i.e. git push origin main --tags

docker-build:
	@echo Building a new docker image
	docker build -t $(DOCKER_IMAGE_NAME):$(CURRENT_VERSION) -t $(DOCKER_IMAGE_NAME):latest .
	@echo Docker image built

docker-push:
	@echo Pushing a new docker image
	docker push $(DOCKER_IMAGE_NAME):$(CURRENT_VERSION)
	docker push $(DOCKER_IMAGE_NAME):latest
	@echo Docker image pushed

python-build:
	@echo Building a python package
	python setup.py sdist
	@echo Python package built
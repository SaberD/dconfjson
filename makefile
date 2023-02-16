all: build

.PHONY: build
build:
	python3 -m build

.PHONY: upload
upload:
	twine upload dist/*
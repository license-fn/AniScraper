build:
	python setup.py bdist_wheel sdist

install: build
	pip install dist/ani_scraper-0.0.1-py3-none-any.whl

.PHONY: build install
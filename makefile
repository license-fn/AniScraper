build:
	python3 setup.py bdist_wheel sdist

install:
	pip3 install dist/ani_scraper-0.0.1-py3-none-any.whl

.PHONY: build install
.PHONY: test lint run

test:
	python -m unittest discover -s tests -p '*_tests.py'

lint:
	python -m py_compile $(shell find . -name '*.py' -not -path './.git/*')

run:
	python cmd/control_plane_server.py

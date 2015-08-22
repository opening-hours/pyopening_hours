.PHONY: default test package dependencies-get

default: dependencies-get test

README.rst: README.md

%.rst: %.md
	pandoc --from=markdown --to=rst --output="$@" "$<"

test:
	./setup.py test

package: README.rst
	./setup.py sdist

dependencies-get:
	pip install .
	npm install opening_hours

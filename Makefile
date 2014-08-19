
default: installDependencies test

README.rst: README.md

%.rst: %.md
	pandoc --from=markdown --to=rst --output="$@" "$<"

test:
	./setup.py test

package: README.rst
	./setup.py sdist

installDependencies: pyopening_hours/node_modules/opening_hours README.rst
	pip install .

pyopening_hours/node_modules/opening_hours:
	npm install opening_hours

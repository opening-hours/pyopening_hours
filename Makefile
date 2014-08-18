
default: installDependencies test

test:
	./setup.py test

package:
	./setup.py sdist

installDependencies: pyopening_hours/node_modules/opening_hours
	pip install .

pyopening_hours/node_modules/opening_hours:
	npm install opening_hours

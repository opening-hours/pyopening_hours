
default: installDependencies test

test:
	./setup.py test

package:
	./setup.py sdist

installDependencies: pyopening_hours/node_modules/opening_hours

pyopening_hours/node_modules/opening_hours:
	npm install opening_hours

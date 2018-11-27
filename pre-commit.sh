#!/bin/sh

# pre-commit.sh
pylint src --rcfile=pylint_settings.rc

cd src
python3 -m pytest --cov=.
RESULT=$?

if [ $RESULT -ne 0 ]
then
	echo "Pre-commit hook failed"
	exit 1
fi

exit 0
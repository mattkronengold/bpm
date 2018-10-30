#!/bin/sh

# pre-commit.sh
git stash -q --keep-index

pylint src --rcfile=pylint_settings.rc
RESULT1=$?

pytest
RESULT2=$?

git stash pop -q

if [ $RESULT1 -ne 0 ] || [ $RESULT2 -ne 0 ]
then
	echo "Pre-commit hook failed"
	exit 1
fi

exit 0
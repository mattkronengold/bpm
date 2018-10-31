#!/bin/sh

touch travis_ci_output/${TRAVIS_BUILD_NUMBER}_pylint_out.txt
touch travis_ci_output/${TRAVIS_BUILD_NUMBER}_pytest_out.txt

pylint src --rcfile=pylint_settings.rc 2>&1 | tee travis_ci_output/${TRAVIS_BUILD_NUMBER}_pylint_out.txt
RESULT1=${PIPESTATUS[0]}

cd src
pytest 2>&1 | tee ../travis_ci_output/${TRAVIS_BUILD_NUMBER}_pytest_out.txt
RESULT2=${PIPESTATUS[0]}

cd ..

if [ $RESULT1 -ne 0 ] || [ $RESULT2 -ne 0 ]
then
	echo "One or more tests failed."
	exit 1
fi

exit 0
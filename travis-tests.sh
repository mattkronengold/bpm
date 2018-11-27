#!/bin/sh

touch travis_ci_output/${TRAVIS_BUILD_NUMBER}_pylint_out.txt
touch travis_ci_output/${TRAVIS_BUILD_NUMBER}_pytest_out.txt

pylint src --rcfile=pylint_settings.rc 2>&1 | tee travis_ci_output/${TRAVIS_BUILD_NUMBER}_pylint_out.txt

cd src
python3 -m pytest --cov=. 2>&1 | tee ../travis_ci_output/${TRAVIS_BUILD_NUMBER}_pytest_out.txt
RESULT=${PIPESTATUS[0]}

cd ..

if [ $RESULT -ne 0 ]
then
	echo "One or more tests failed."
	exit 1
fi

exit 0
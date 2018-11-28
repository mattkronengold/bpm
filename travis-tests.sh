#!/bin/sh

touch ${TRAVIS_BUILD_NUMBER}_pylint_out.txt
touch ${TRAVIS_BUILD_NUMBER}_pytest_out.txt

pylint src --rcfile=pylint_settings.rc 2>&1 | tee ${TRAVIS_BUILD_NUMBER}_pylint_out.txt

cd src
python3 -m pytest --cov=. 2>&1 | tee ../${TRAVIS_BUILD_NUMBER}_pytest_out.txt
RESULT=${PIPESTATUS[0]}

cd ..

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git remote add origin-ci https://${GITHUB_TOKEN}@github.com/mattkronengold/bpm.git
git fetch origin-ci

git checkout travis_ci_output
git add *.txt
git commit -m "Travis build: $TRAVIS_BUILD_NUMBER"
git push

if [ $RESULT -ne 0 ]
then
	echo "One or more tests failed."
	exit 1
fi

exit 0
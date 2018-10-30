git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git commit -a -m 'Travis build: $TRAVIS_BUILD_NUMBER [travis skip]'

git remote add origin https://${GH_TOKEN}@github.com/mattkronengold/bpm.git
git push --quiet --set-upstream origin master
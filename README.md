# bpm
BPM: A Better Playlist Builder

## Pre-commit hook
To install the pre-commit hook, use command: 

`ln -s ../../pre-commit.sh .git/hooks/pre-commit`

Test commands are maintained in the file pre-commit.sh

## Testing

Test using the following two commands:
```
pylint src
pytest
```

Pytests runs any files with the naming conventions `test_*.py` or `*_test.py`.

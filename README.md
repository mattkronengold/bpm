# bpm
BPM: A Better Playlist Builder

## Installing
1. Clone the github repository
	* ```git clone git@github.com:mattkronengold/bpm.git```
2. Install python & pip
3. Navigate to the bpm directory
4. Install requirements
	* ```pip install -r requirements.txt```

## Running
1. Navigate to the bpm directory
2. Navigate to the src directory
	* ```cd src```
3. Launch the program
	* ```python3 bpm.py```

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

Pytests runs tests in all files with the naming conventions `test_*.py` or `*_test.py`.

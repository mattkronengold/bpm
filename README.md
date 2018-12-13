# bpm
BPM: A Better Playlist Builder

## Installing
1. Clone the github repository
	* ```git clone git@github.com:mattkronengold/bpm.git```
2. Install python3 & pip3
3. Navigate to the bpm directory
4. Install requirements
	* ```pip install -r requirements.txt```
	* Depending on your system configuration, you may need to use the command: ```pip3 install -r requirements.txt```

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
1. Navigate to the bpm directory
2. Run pylint
	* ```pylint src --rcfile=pylint_settings.rc```
3. Run pytest
	* ```cd src```
	* ```python3 -m pytest --cov=.```
	* Pytests runs tests in all files with the naming conventions `test_*.py` or `*_test.py`.

Both of these tests are un in the pre-commit hook which can be executed with:
```./pre-commit.sh```

## Operating
1. Enter a username for your BPM account (new user) or your BPM username (returning user).
2. Your browser will direct you to authenticate with your Spotify credentials. Copy and paste the authentication code into the terminal. The format will be https://localhost/?code=<YOUR AUTHENTICATION CODE>
3. Enter your preference of genre, playlist length, start speed, and end speed.
4. Wait while we scan your library to build your custom playlist.
5. Review your generated playlist and specify whether you want to swap out a song, swap out a song and dislike it, change the parameters for your playlist, or continue with the playlist that was generated.
6. Enter a name for your playlist.
7. Choose if you'd like to open up Spotify and start listening right away or wait until your workout.

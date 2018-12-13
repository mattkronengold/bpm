# BPM
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
1. Welcome to BPM! If you are a new user, please enter a username for your BPM account. If you are a returning user, please enter your BPM username.
2. Your browser will direct you to authenticate with your Spotify credentials. Copy and paste the authentication code into the terminal. The format will be of the form: “https://localhost/?code=”<CODE>
3. You will be asked to choose from a menu of genres for your playlist. Please enter an integer corresponding to one of the menu items.
4. You will be asked to specify the length of your playlist in minutes. Please enter an integer between 5 and 90 minutes.
5. You will be asked to enter the start and end speed of your run in steps per minute. Please enter an integer between 50 and 300.
6. Wait while we scan your library to build your custom playlist.
7. You will be shown your generated playlist and a menu of options to swap out a song, swap out a song and dislike it for future playlists, go back and change the parameters, or keep your playlist the way it is.
8. You will be asked to enter a name for your playlist. Please enter a unique string.
You will be asked whether you’d like to open Spotify and start listening to your playlist. Please enter an integer corresponding to yes or no.
9. At any time in this process, please enter “logout” to logout of BPM. 


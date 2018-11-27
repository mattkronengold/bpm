#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:02:30 2018

@author: mattkronengold
"""
from __future__ import print_function
import auth
from inputs import get_inputs
from generation import generate_playlist, print_playlist
from review import start_review, save_playlist

def main():
    """
        Run BPM application
    """

    if auth.welcome():
        token = auth.get_current_user_token()

        inputs = get_inputs()

        generation = generate_playlist(token, inputs)
        library = generation["library"]
        playlist = generation["playlist"]

        print("Your generated playlist is:")
        print_playlist(playlist)

        #i = 1
        #for track in playlist:
        #   print(i, ": ", track['name'] + " (" + str(track['bpm']) + " BPM)")
        #    i += 1

        playlist = start_review(playlist, library)
        save_playlist(playlist)

        #create_playlist(token, ids)


if __name__ == "__main__":
    main()

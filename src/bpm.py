#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:02:30 2018

@author: mattkronengold
"""
from __future__ import print_function
import auth
from inputs import get_inputs
from generation import run_gen
from review import start_review, print_playlist
from create_playlist import create_playlist
from playlist_cache import get_playlist_cache, cache_playlist, check_cache
from database import verify_tables

def main():
    """
        Run BPM application
    """

    verify_tables('bpm.db')

    if auth.welcome():
        token = auth.get_current_user_token()

        if(check_cache(print_playlist)):
            playlist = get_playlist_cache()
            create_playlist(token, playlist)
            print("Let's create another playlist!")

        inputs = get_inputs()

        generation = run_gen(token, inputs)
        library = generation["library"]
        playlist = generation["playlist"]

        print("Your generated playlist is:")
        print_playlist(playlist)

        playlist = start_review(playlist, library)
        cache_playlist(playlist)

        create_playlist(token, playlist)


if __name__ == "__main__":
    main()

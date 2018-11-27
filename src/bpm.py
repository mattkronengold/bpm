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

def main():
    """
        Run BPM application
    """

    if auth.welcome():
        token = auth.get_current_user_token()

        inputs = get_inputs()

        generation = run_gen(token, inputs)
        library = generation["library"]
        playlist = generation["playlist"]

        print("Your generated playlist is:")
        print_playlist(playlist)

        playlist = start_review(playlist, library)

        create_playlist(token, playlist)


if __name__ == "__main__":
    main()

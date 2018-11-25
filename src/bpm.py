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
from review import start_review, save_playlist

def main():
    """Run BPM application"""

    if auth.welcome():
        inputs = get_inputs()
        token = auth.get_current_user_token()
        generation = run_gen(token, inputs["genre"], inputs["length"], \
            inputs["start_speed"], inputs["end_speed"])
        playlist = generation["playlist"]
        library = generation["library"]
        names = [track["name"] for track in playlist]
        print("Your generated playlist is:")
        for i, _ in enumerate(names):
            print(i, ": ", names[i])
        print()

        playlist = start_review(names, library)
        save_playlist(playlist)

        #create_playlist(token, ids)


main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:02:30 2018

@author: mattkronengold
"""
from __future__ import print_function
import auth
from inputs import get_length, get_genre, get_speed
from generation import run_gen

def main():
    """Run BPM application"""

    if auth.welcome():
        genre = get_genre()
        print()
        length = get_length()
        print()
        start_speed = get_speed('start')
        print()
        end_speed = get_speed('end')
        print()

        token = auth.get_current_user_token()

        playlist = run_gen(token, genre, length, start_speed, end_speed)
        names = [track["name"] for track in playlist]

        print("Your generated playlist is:")
        print(names)
        print()

        #create_playlist(token, ids)

main()

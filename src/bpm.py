#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:02:30 2018

@author: mattkronengold
"""
from auth import welcome
from inputs import get_length, get_genre, get_speed

def main():
    if(welcome()):
	    genre = get_genre()
	    length = get_length()
	    start_speed = get_speed('start')
	    end_speed = get_speed('end')

main()
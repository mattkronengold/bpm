#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:47:54 2018

@author: mattkronengold
"""
from __future__ import print_function
from collections import defaultdict
import random
import spotipy

GENRES = {0: "any",
          1: "rock",
          2: "rap",
          3: "pop",
          4: "edm",
          5: "latin",
          6: "country",
          7: "r&b"}

def get_genres(spotify, track):
    """Get genres from the artists of a track"""

    artists = track["artists"]
    artist_ids = []
    genres = []

    for artist in artists:
        artist_ids.append(artist["id"])


    for artist_id in artist_ids:
        artist_full = spotify.artist(artist_id)
        genres.extend(artist_full["genres"])

    return genres

def has_genre(spotify, track, genre):
    """Returns true if track satisfies the given genre code"""

    if genre == 0:
        return True

    track_genres = get_genres(spotify, track)
    target_genre = GENRES[genre]

    for track_genre in track_genres:
        if target_genre in track_genre:
            return True

    return False

def scan_library(spotify, genre, start_speed, end_speed, reverse):
    """Scan library for potential songs"""

    print("Scanning library")

    library = defaultdict(list)

    results = spotify.current_user_saved_tracks(limit=20, offset=0)

    # Currently limit to scanning 100 tracks
    while True:
        for result in results["items"]:

            track = result["track"]

            if not has_genre(spotify, track, genre):
                continue

            tid = track["id"]
            name = track["name"]
            duration = track["duration_ms"]
            features = spotify.audio_features([tid])
            bpm = int(features[0]["tempo"])

            # Round to 10's place
            bpm = round(bpm/10) * 10

            if reverse:
                if bpm > start_speed or bpm < end_speed:
                    continue
            else:
                if bpm < start_speed or bpm > end_speed:
                    continue

            library[bpm].append({"tid": tid,
                                 "name": name,
                                 "duration": duration,
                                 "bpm": bpm})

        if not results["next"]:
            break
        else:
            results = spotify.next(results)

    print("Library scanned\n")
    return library

def gen_playlist(library, length, reverse):
    """Generates a playlist from given inputs

    Argument legnth should be in ms
    """

    print("Generating playlist")

    all_speeds = list(library.keys())
    all_speeds.sort(reverse=reverse)

    playlist = defaultdict(list)

    total_length = 0
    stop = False

    while not stop and all_speeds:

        for speed in all_speeds:

            tracks = library[speed]
            random.shuffle(tracks)

            if not tracks:
                all_speeds.remove(speed)
                continue

            track = tracks[0]
            tracks.remove(track)

            playlist[speed].append(track)
            total_length += track["duration"]

            if total_length > length:
                stop = True
                break

    if total_length < length:
        print("Not enough songs available to generate full playlist\n")
    else:
        print("Playlist generated\n")

    final_playlist = []
    for group in playlist.values():
        final_playlist.extend(group)


    return final_playlist

def run_gen(token, inputs):
    """
        Generate spotify playlist from given inputs.
    """

    spotify = spotipy.Spotify(auth=token)

    genre = inputs["genre"]
    length = inputs["length"]
    start_speed = inputs["start_speed"]
    end_speed = inputs["end_speed"]

    # Convert to ms
    length = length * 60000

    reverse = start_speed > end_speed

    library = scan_library(spotify, genre, start_speed, end_speed, reverse)
    playlist = gen_playlist(library, length, reverse)

    return {"library": library, "playlist": playlist}

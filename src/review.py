'''

@author: alanaanderson, katiepfleger

'''
from logout import check_input
from inputs import get_inputs
from auth import get_current_user_token
from generation import run_gen
from database import insert_dislike

def start_review(playlist, library):
    '''
        Checks if user wants to make any changes to the playlist
    '''
    print('Would you like to make any changes to your playlist?')
    print('0:\tYes, I want to swap a song')
    print('1:\tYes, I want to swap a song and dislike it')
    print('2:\tYes, I want to change the parameters')
    print('3:\tNo, I like it the way it is')
    resp = input()
    print()
    check_input(resp)
    if resp in ['0', '1']:
        song_index = get_song_index()
        while song_index not in range(len(playlist)):
            print("Please enter a valid input.")
            song_index = get_song_index()

        song_dict = playlist[song_index]

        if resp == '1':
            insert_dislike('bpm.db', song_dict['tid'])

        song_bpm = song_dict["bpm"]
        first_key = list(library.keys())[0]
        if library[song_bpm]:
            swap_song(playlist, library, song_bpm, song_index)
        elif library[first_key]:
            swap_song(playlist, library, first_key, song_index)
        else:
            print("There are not enough songs in your library.")
            print("Would you like to: ")
            print("0: forcibly remove the song (your playlist length will be altered)")
            print("1: keep the current playlist")
            option = input()
            print()
            check_input(option)
            if option == '0':
                playlist.remove(song_dict)
                print("Your new playlist is:")
                print_playlist(playlist)
                return start_review(playlist, library)
            else:
                print("Your playlist is:")
                print_playlist(playlist)
                return start_review(playlist, library)
        return start_review(playlist, library)
    elif resp == '2':
        inputs = get_inputs()
        token = get_current_user_token()

        generation = run_gen(token, inputs)
        library = generation["library"]
        playlist = generation["playlist"]

        print("Your generated playlist is: ")
        print_playlist(playlist)
        return start_review(playlist, library)
    elif resp == '3':
        # return playlist to save
        return playlist
    else:
        print("Please enter a valid input.")
        return start_review(playlist, library)

def swap_song(playlist, library, key, song_index):
    """
        Swaps current song at song_index with
        the song at the specified key in the library.
    """

    song = library[key][0]
    playlist[song_index] = song
    library[key].remove(song)
    print("Your new playlist is:")
    print_playlist(playlist)

def get_song_index():
    """
        Gets song_index to swap from user.
    """
    song_index = input('Please enter the number of the song you want to swap:\n')
    print()
    check_input(song_index)
    try:
        song_index = int(song_index)
    except ValueError:
        print('Please enter an integer value.')
        return get_song_index()

    return song_index

def print_playlist(playlist):
    """
        Print formatted playlist.
    """
    i = 0
    for track in playlist:
        print(i, ": ", track['name'] + " (" + str(track['bpm']) + " BPM)")
        i += 1
    print()

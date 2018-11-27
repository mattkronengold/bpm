'''

@author: alanaanderson, katiepfleger

'''
from logout import check_input
from inputs import get_inputs
from auth import get_current_user_token
from generation import run_gen

def start_review(playlist, library):
    '''
        Checks if user wants to make any changes to the playlist
    '''
    print('Would you like to make any changes to your playlist?')
    print('0:\tYes, I want to swap a song')
    print('1:\tYes, I want to change the parameters')
    print('2:\tNo, I like it the way it is')
    resp = input()
    print()
    check_input(resp)
    if resp == '0':
        song_index = input('Please enter the number of the song you want to swap:\n')
        print()
        check_input(song_index)
        song_index = int(song_index)
        song_dict = playlist[song_index]
        for k in library:
            if library[k]:
                song = library[k][0]
                playlist[song_index] = song
                library[k].remove(song)
                print("Your new playlist is:")
                print_playlist(playlist)
                break
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
    elif resp == '1':
        inputs = get_inputs()
        token = get_current_user_token()

        generation = run_gen(token, inputs)
        library = generation["library"]
        playlist = generation["playlist"]

        print("Your generated playlist is: ")
        print_playlist(playlist)
        return start_review(playlist, library)
    elif resp == '2':
        # return playlist to save
        return playlist
    else:
        print("Please enter a valid input.")
        return start_review(playlist, library)

def print_playlist(playlist):
    """
        Print formatted playlist.
    """
    i = 1
    for track in playlist:
        print(i, ": ", track['name'] + " (" + str(track['bpm']) + " BPM)")
        i += 1
    print()

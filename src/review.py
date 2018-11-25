'''

@author: alanaanderson, katiepfleger

'''
from logout import check_input
from inputs import get_inputs
from auth import get_current_user_token
from generation import run_gen

def start_review(names, library):
    '''
        Checks if user wants to make any changes to the playlist
    '''
    print('Would you like to make any changes to your playlist?')
    print('0:\tYes, I want to swap a song')
    print('1:\tYes, I want to change the parameters')
    print('2:\tNo, I like it the way it is')
    resp = input()
    check_input(resp)
    if resp == '0':
        song_index = int(input('Please enter the number of the song you want to swap:\n'))
        song_name = names[song_index]
        for k in library:
            if library[k]:
                song = library[k][0]
                names[song_index] = song["name"]
                library[k].remove(song)
                print("Your new playlist is:")
                for i, _ in enumerate(names):
                    print(i, ": ", names[i])
                print()
                break
            else:
                option = input("There are not enough songs in your library. \
                    Would you like to: \n 0: forcibly remove the song (your playlist length will be altered) \n \
                    1: keep the current playlist \n")
                if option == '0':
                    names.remove(song_name)
                    print("Your new playlist is:")
                    for i, _ in enumerate(names):
                        print(i, ": ", names[i])
                        print()
                    return start_review(names, library)
                else:
                    print("Your playlist is:")
                    for i, _ in enumerate(names):
                        print(i, ": ", names[i])
                    print()
                    return start_review(names, library)
        return start_review(names, library)
    if resp == '1':
        inputs = get_inputs()
        token = get_current_user_token()
        generation = run_gen(token, inputs["genre"], inputs["length"],\
            inputs["start_speed"], inputs["end_speed"])
        playlist = generation["playlist"]
        library = generation["library"]
        names = [track["name"] for track in playlist]

        print("Your generated playlist is:")
        for i, _ in enumerate(names):
            print(i, ": ", names[i])
        print()
        return start_review(names, library)
    if resp == '2':
        # return playlist to save
        return names

def save_playlist(playlist):
    '''
        Save playlist to Spotify.
    '''
    return playlist

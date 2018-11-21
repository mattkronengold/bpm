'''

@author: alanaanderson, katiepfleger

'''
from logout import check_input

def start_review():
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
        # swap song
        print('swap song')
    if resp == '1':
        # call enter inputs
        print('enter inputs')
    if resp == '2':
        # call save playlist
        print('create playlist')

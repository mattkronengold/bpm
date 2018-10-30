'''

@author: katiepfleger

'''
from __future__ import print_function
from logout import check_input

def get_length():
    '''
    	Gets length of playlist from user.
    '''
    length = input('Enter the length of your workout in minutes: \n')
    check_input(length)
    try:
        length = int(length)
        if length in range(5, 91):
            return length
        else:
            print('Please enter a duration between 5-90.')
            return get_length()
    except ValueError:
        print('Please enter a duration between 5-90.')
        return get_length()

def get_genre():
    '''
    	Gets genre preference from user input.
    '''
    print('Enter your genre preference: ')
    genre = input('0: \t No Preference \n'\
				  '1: \t Rock \n' \
				  '2: \t Hip Hop \n' \
				  '3: \t Pop \n' \
				  '4: \t Dance/Electronic \n' \
				  '5: \t Latin \n' \
				  '6: \t Country \n' \
				  '7: \t R&B \n')
    check_input(genre)
    try:
        genre = int(genre)
        if genre in range(0, 8):
            return genre
        else:
            print('Please enter an integer value corresponding to the following genres: ')
            return get_genre()
    except ValueError:
        print('Please enter an integer value corresponding to the following genres: ')
        return get_genre()


def get_speed(start_or_end):
    '''
        Gets start or end speed from user input.
    '''
    speed = input('Enter the ' + start_or_end + \
        ' speed of your workout in steps per minute (SPM): \n')
    check_input(speed)
    try:
        speed = int(speed)
        if speed in range(50, 301):
            return speed
        else:
            print('Please enter a speed between 50-300 SPM')
            return get_speed(start_or_end)
    except ValueError:
        print('Please enter a speed between 50-300 SPM')
        return get_speed(start_or_end)

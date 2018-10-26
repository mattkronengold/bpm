import sys

print('Welcome to BPM!')

user_type = input('Are you a new user (0) or a returning user (1)? ')

if (user_type == '0'):
    print('Do you have a Spotify account?')
    print('0\tyes')
    print('1\tno')
    has_account = input()

    if(has_account == '0'):
        print('Now we do login')

    else:
        print('Please sign up for a Spotify account and come back.')

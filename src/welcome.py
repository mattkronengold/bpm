import sys

print('Welcome to BPM!')

user_type = input('Are you a new user (0) or a returning user (1)?\n')

if (user_type == '0'):
    print('Do you have a Spotify account?')
    print('0\tyes')
    print('1\tno')
    has_account = input()

if (has_account == '0'):
	print('Now we do login...')

else:
	print('Please sign up for a Spotify account and return.')


client_id = 482102fb45cb45fdb465ef73801f4665 
response_type = code
redirect_uri = http://localhost/ 

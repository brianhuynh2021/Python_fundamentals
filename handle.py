def get_handle():
    handle_1 = input('Please enter your Twitter username: ')
    return handle_1

h = get_handle()
length = len(h)
print('Your Twitter username has', length, 'characters')

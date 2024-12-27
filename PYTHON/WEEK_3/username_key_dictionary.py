def items(password):
    print("Items in dictionary:")
    for i in password:
        print(f'{i}:{password[i]}  ', end='')
    print('\n')


def keys(password):
    print("Keys in dictionary:")
    for i in password:
        print(i, end='  ')
    print('\n')


def values(dictionary):
    print("Values in dictionary:")
    for i in dictionary:
        print(dictionary[i], end='  ')
    print('\n')


def get_password(dictionary, username):
    flag = dictionary.get(username, 0)
    if flag:
        print(f'username:{username}  password:{flag}')
    else:
        print(f'Username is not found')
    print()


def change_password(dictionary, username, new_password):
    if username in dictionary:
        dictionary[username] = new_password
        print(dictionary)
    else:
        print("User name is not found")


passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankit': 'intelligent'}

items(passwd)
values(passwd)
keys(passwd)
get_password(passwd, "kumar")
change_password(passwd, 'ankit', 'bad boy')

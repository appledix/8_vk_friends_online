import vk
import itertools
import getpass

APP_ID = 5672090


def get_user_login():
    return input("Login for 'https://vk.com': ")

def get_user_password():
    return getpass.getpass(prompt="Password for 'https://vk.com': ", stream=None)

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope=2
        )
    api = vk.API(session)
    online_friends_ids = api.friends.getOnline()
    return api.users.get(user_ids=online_friends_ids)

def output_friends_to_console(friends_online):
    print("Friends online:")
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])
    return


if __name__ == '__main__':
    while True:
        login = get_user_login()
        if login:
            break
    while True:
        password = get_user_password()
        if password:
            break
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)

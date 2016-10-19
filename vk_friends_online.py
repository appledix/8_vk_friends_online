import vk
import itertools
import getpass

APP_ID = 5672090


def get_user_login():
    while True:
        login = input("Login for 'https://vk.com': ")
        if login: break
    return login

def get_user_password():
    while True:
        password = getpass.getpass(prompt="Password for 'https://vk.com': ", stream=None)
        if password: break
    return password

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password
        )
    api = vk.API(session)
    friends = api.friends.get(fields="online")
    online_friends = list(itertools.filterfalse(lambda friend: friend['online'] != 1, friends))
    return online_friends

def output_friends_to_console(friends_online):
    print("Друзья онлайн:")
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])
    return


if __name__ == '__main__':
    while True:
        login = get_user_login()
        password = get_user_password()
        try:
            friends_online = get_online_friends(login, password)
        except Exception:
            continue
        else:
            output_friends_to_console(friends_online)
            break

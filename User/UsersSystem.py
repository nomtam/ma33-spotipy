import json

import SearchAPI
import configuration
from OptionsMenu import OptionsMenu


class UsersSystem:
    def __init__(self):
        self.file_location = configuration.users_file_location
        self.users = self.load_users()

    def sign_up(self, user):
        if user.user_name in self.users.keys():
            raise UserNameTakenException(f"{user.user_name} is taken by another user.")
        with open(self.file_location, 'a') as users_file:
            users_file.write(json.dumps({'user_name': user.user_name, 'type': user.type}))

    def login(self, user_name):
        if user_name in self.users.keys():
            print(
                f"hello {user_name}! welcome to spotipy. you can now use our api.\n here is a menu with your options")
            OptionsMenu(self.users[user_name]).show_options_menu()
        else:
            raise UserDoesntExistsException(f"user:{user_name} dose not exists in the system.")

    def load_users(self):
        users = {}
        try:
            with open(self.file_location, 'r') as users_file:
                for line in users_file:
                    user_dic = json.loads(line)
                    users[user_dic['user_name']] = user_dic
        except IOError:
            pass  # no users in the system yet
        return users


class UserDoesntExistsException(Exception):
    pass


class UserNameTakenException(Exception):
    pass

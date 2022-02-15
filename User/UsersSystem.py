import json

import configuration
from Menus.UIMenu import UIMenu


class UsersSystem:
    def __init__(self):
        self.file_location = configuration.users_file_location
        self.users = self.load_users()

    def sign_up(self, user):
        if user.user_name in self.users.keys():
            raise UserNameTakenException(f"{user.user_name} is taken by another user.")
        with open(self.file_location, 'a') as users_file:
            users_file.write(json.dumps({'user_name': user.user_name, 'type': user.type}) + "\n")

    def login(self, user_name):
        if user_name in self.users.keys():
            print(
                f"hello {user_name}! welcome to spotipy. you can now choose the UI.")
            UIMenu(self.users[user_name]).show_UIMenu()
        else:
            raise UserDoesntExistsException(f"user:{user_name} dose not exists in the system.")

    def load_users(self):
        users = {}
        try:
            # CR:
            """
            If you would have made a good json format. For example:
            { "users": [
                    {"user_name": "tomer", "type": "free"},
                    {"user_name": "guy", "type": "free"},
                    {"user_name": "elad", "type": "premium"}
                    ] 
            you could load all in one line with json.load
            """
            with open(self.file_location, 'r') as users_file:
                for line in users_file:
                    user_dic = json.loads(line)
                    # CR: config. also, if you do what i suggestted above you could do this with list comprehension
                    users[user_dic['user_name']] = user_dic
        except IOError:
            # CR: and what the IOERror is because the file is corrupted? Bad exception handling.
            pass  # no users in the system yet
        return users


# CR: exceptions should be in a exception module
class UserDoesntExistsException(Exception):
    pass


class UserNameTakenException(Exception):
    pass

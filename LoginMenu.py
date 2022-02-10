from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

from User.FreeUser import FreeUser
from User.PremiumUser import PremiumUser
from User.UsersSystem import UsersSystem


class LoginMenu:
    def __init__(self):
        pass

    def show_login_menu(self):
        login_menu = ConsoleMenu('login-menu')
        login = FunctionItem("login", self.login)
        sign_up = FunctionItem('sign up', self.sign_up)
        login_menu.append_item(login)
        login_menu.append_item(sign_up)
        login_menu.show()

    def sign_up(self):
        user_name = input("enter user name: ")
        user_type = input("enter user type: ")
        UsersSystem().sign_up(users[user_type](user_name))

    def login(self):
        user_name = input("enter user name: ")
        UsersSystem().login(user_name)


users = {
    'free': FreeUser,
    'premium': PremiumUser
}

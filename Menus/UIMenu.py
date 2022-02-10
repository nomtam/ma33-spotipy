from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

from Menus.OptionsMenu import OptionsMenu
import SearchAPI


class UIMenu:
    def __init__(self, user):
        self.user = user

    def show_UIMenu(self):
        ui_menu = ConsoleMenu('ui-menu')
        api = FunctionItem('use the searching api', SearchAPI.start_api)
        options_menu = FunctionItem('use the options menu', OptionsMenu(self.user).show_options_menu)
        ui_menu.append_item(options_menu)
        ui_menu.append_item(api)
        ui_menu.show()

from main_menu import MainMenu

class MenuFactory:
    """
    This class is a hack to avoid circular imports when it's time to go back to the menu
    """
    @staticmethod
    def create_main_menu():
        return MainMenu()

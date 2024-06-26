class ToolbarSettings:
    """
    Настройки редактора.

    Attributes:
        настройки_по_умолчанию (bool): Флаг, указывающий, используются ли настройки по умолчанию.
        язык (str): Выбранный язык для редактора.
    """

    def __init__(self):
        """
        Инициализация класса настроек редактора.
        """
        self.настройки_по_умолчанию = True
        self.язык = 'Русский'

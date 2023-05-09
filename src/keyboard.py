from src.item import Item


class MixinLog:
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        self.__language = "RU" if self.__language == "EN" else "EN"
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        self.__language = language
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

    def change_language(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

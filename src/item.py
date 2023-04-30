import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Устанавливает геттер для названия товара.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Устанавливает сеттер для названия товара с проверкой на кол-во символов.
        """
        if len(name) > 10:
            print("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует объекты класса из списка.
        """
        with open('../src/items.csv', 'r', encoding='cp1251') as file:
            csv_reader = csv.DictReader(file)
            cls.all.clear()
            new_list = list(csv_reader)
            for i in range(len(new_list)):
                name = new_list[i]["name"]
                price = float(new_list[i]["price"])
                quantity = int(new_list[i]["quantity"])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """
        Превращает строку в число.
        """
        if "." in string:
            string_float = float(string)
            string_int = int(string_float)
            return string_int
        else:
            string_int = int(string)
            return string_int

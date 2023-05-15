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
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None

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
            raise ValueError("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_path='../src/items.csv'):
        """
        Инициализирует объекты класса из списка.
        """
        required_columns = ['name', 'price', 'quantity']
        try:
            open(file_path)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")
        else:
            with open(file_path, 'r', encoding='cp1251') as file:
                csv_reader = csv.DictReader(file)
                headers = csv_reader.fieldnames

                for column in required_columns:
                    if column not in headers:
                        raise InstantiateCSVError

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


class InstantiateCSVError(Exception):
    """Выводит ошибку при поврежденном файле"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл items.csv поврежден'

    def __str__(self):
        return self.message

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"{self._name}: {self._price}"

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

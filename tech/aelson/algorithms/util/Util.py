from typing import List
from tech.aelson.algorithms.model.Product import Product


class Util:
    @staticmethod
    def swap(products: List[Product], first: int, second: int):
        print("<-> Swapping element", first, "with", second)

        first_product = products[first]
        second_product = products[second]

        print("<-> Swapping product", first_product.get_name(), "with", second_product.get_name())

        products[first] = second_product
        products[second] = first_product

        print("------------------------------------")

    @staticmethod
    def print_array(array_title: str, products: List[Product]):
        print(array_title)
        for product in products:
            print(product.get_name(), "costs", product.get_price())

    @staticmethod
    def get_unsorted_products() -> List[Product]:
        return [
            Product("Ford Escape", 30000),
            Product("Toyota Corolla", 20000),
            Product("Audi Q5", 45000),
            Product("Honda Civic", 30000),
            Product("Tesla Model 3", 50000)
        ]

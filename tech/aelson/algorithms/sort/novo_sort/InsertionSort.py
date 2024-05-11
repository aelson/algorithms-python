from typing import List
from tech.aelson.algorithms.model.Product import Product
from tech.aelson.algorithms.util.Util import Util


class InsertionSort:
    @staticmethod
    def execute(products: List[Product], number_of_elements: int):
        for current in range(1, number_of_elements):
            print("I am in the element", current)
            element_being_analysed = current
            while element_being_analysed > 0 and products[element_being_analysed].get_price() < products[element_being_analysed - 1].get_price():
                Util.swap(products, element_being_analysed, element_being_analysed - 1)
                element_being_analysed -= 1

from typing import List
from tech.aelson.algorithms.search.find_smallest.find_smallest import FindSmallest
from tech.aelson.algorithms.model.product import Product
from tech.aelson.algorithms.util.util import Util


class SelectionSort:
    @staticmethod
    def execute(products: List[Product], number_of_elements: int):
        for current in range(number_of_elements - 1):
            print("I am in the element", current)

            smallest = FindSmallest.execute(products, current, number_of_elements - 1)

            Util.swap(products, current, smallest)

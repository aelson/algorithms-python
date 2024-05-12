from typing import List
from tech.aelson.algorithms.model.product import Product


class FindSmallest:
    @staticmethod
    def execute(products: List[Product], start: int, end: int) -> int:
        smallest = start
        for index in range(start, end + 1):
            if products[index].get_price() < products[smallest].get_price():
                smallest = index
        return smallest

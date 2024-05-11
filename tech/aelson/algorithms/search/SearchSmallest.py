from typing import List
from tech.aelson.algorithms.model.Product import Product


class SearchSmallest:
    @staticmethod
    def execute(products: List[Product], start: int, end: int) -> int:
        smallest = start
        for atual in range(start, end + 1):
            if products[atual].get_price() < products[smallest].get_price():
                smallest = atual
        return smallest

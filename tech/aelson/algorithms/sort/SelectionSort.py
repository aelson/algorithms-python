from typing import List
from tech.aelson.algorithms.search.SearchSmallest import SearchSmallest
from tech.aelson.algorithms.model.Product import Product


class SelectionSort:
    @staticmethod
    def execute(products: List[Product], number_of_elements: int):
        for current in range(number_of_elements - 1):
            print("I am in the element", current)

            smallest = SearchSmallest.execute(products, current, number_of_elements - 1)

            print("<-> Swapping element", current, "with element", smallest)

            current_product = products[current]
            smallest_product = products[smallest]

            print("<-> Swapping product", current_product.get_name, "with product", smallest_product.get_name)

            products[current] = smallest_product
            products[smallest] = current_product
            print("------------------------------------")

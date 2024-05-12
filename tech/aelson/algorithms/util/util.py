from typing import List
from tech.aelson.algorithms.model.product import Product
from tech.aelson.algorithms.model.grade import Grade


class Util:
    @staticmethod
    def swap(array: List, first: int, second: int):
        print("<-> Swapping element", first, "with", second)

        first_product = array[first]
        second_product = array[second]

        #print("<-> Swapping product", first_product, "with", second_product)

        array[first] = second_product
        array[second] = first_product

        print("------------------------------------")

    @staticmethod
    def print_products_array(array_title: str, products: List[Product]):
        print(array_title)
        for product in products:
            print(product.get_name(), "costs", product.get_price())

    @staticmethod
    def print_grades_array(array_title: str, grades: List[Grade]):
        print(array_title)
        for grade in grades:
            print(grade.get_student_name(), grade.get_result())

    @staticmethod
    def get_unsorted_products() -> List[Product]:
        return [
            Product("Ford Escape", 30000),
            Product("Toyota Corolla", 20000),
            Product("Audi Q5", 45000),
            Product("Honda Civic", 30000),
            Product("Tesla Model 3", 50000)
        ]

    @staticmethod
    def get_unsorted_grades(special_grade):
        return [
            Grade("andre", 4),
            Grade("carlos", 8.5),
            Grade("ana", 10),
            Grade("jonas", 3),
            Grade("juliana", 6.7),
            Grade("lucia", 9.3),
            Grade("paulo", 9),
            Grade("mariana", 5),
            special_grade,
        ]

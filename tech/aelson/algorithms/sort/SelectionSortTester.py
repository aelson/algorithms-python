from typing import List
from tech.aelson.algorithms.sort.SelectionSort import SelectionSort
from tech.aelson.algorithms.model.Product import Product


def main():
    products = [
        Product("Ford Escape", 30000),
        Product("Toyota Corolla", 20000),
        Product("Audi Q5", 45000),
        Product("Honda Civic", 30000),
        Product("Tesla Model 3", 50000),
    ]

    print("Original array: ")
    for product in products:
        print(product.get_name() + " costs " + str(product.get_price()))

    SelectionSort.execute(products, len(products))

    print("Sorted array: ")
    for product in products:
        print(product.get_name() + " costs " + str(product.get_price()))


if __name__ == "__main__":
    main()

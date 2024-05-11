from tech.aelson.algorithms.util.util import Util
from tech.aelson.algorithms.sort.insertion_sort.insertion_sort import InsertionSort


def main():
    products = Util.get_unsorted_products()
    Util.print_products_array("Original array: ", products)

    InsertionSort.execute(products, len(products))
    Util.print_products_array("Sorted array: ", products)


if __name__ == "__main__":
    main()

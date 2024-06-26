from tech.aelson.algorithms.sort.selection_sort.selection_sort import SelectionSort
from tech.aelson.algorithms.util.util import Util


def main():
    products = Util.get_unsorted_products()
    Util.print_products_array("Original array: ", products)

    SelectionSort.execute(products, len(products))
    Util.print_products_array("Sorted array: ", products)


if __name__ == "__main__":
    main()

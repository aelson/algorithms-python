from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.sort.merge_sort.merge_sort import MergeSort
from tech.aelson.algorithms.util.util import Util


def main():
    first_array = [
        Grade("andre", 4),
        Grade("mariana", 5),
        Grade("carlos", 8.5),
        Grade("paulo", 9),
    ]

    second_array = [
        Grade("jonas", 3),
        Grade("juliana", 6.7),
        Grade("guilherme", 7),
        Grade("lucia", 9.3),
        Grade("ana", 10),
    ]

    Util.print_grades_array("First array: ", first_array)
    Util.print_grades_array("Second array: ", second_array)

    rank = MergeSort.merge_two_arrays(first_array, second_array)
    Util.print_grades_array("Merged array: ", rank)


if __name__ == "__main__":
    main()

from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.sort.quick_sort.quick_sort import QuickSort
from tech.aelson.algorithms.util.util import Util


def main():
    guilherme = Grade("guilherme", 7)
    unsorted_grades = Util.get_unsorted_grades(guilherme)

    QuickSort.execute(unsorted_grades, 0, len(unsorted_grades))
    Util.print_grades_array("Sorted array: ", unsorted_grades)


if __name__ == "__main__":
    main()

from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.sort.merge_sort.merge_sort import MergeSort
from tech.aelson.algorithms.util.util import Util


def main():
    grades = [
        Grade("andre", 4),
        Grade("mariana", 5),
        Grade("carlos", 8.5),
        Grade("paulo", 9),
        Grade("jonas", 3),
        Grade("juliana", 6.7),
        Grade("guilherme", 7),
        Grade("lucia", 9.3),
        Grade("ana", 10)
    ]
    Util.print_grades_array("Grades array: ", grades)

    rank = MergeSort.sort_one_array(grades, 0, 4, len(grades))
    Util.print_grades_array("Sorted array: ", rank)


if __name__ == "__main__":
    main()

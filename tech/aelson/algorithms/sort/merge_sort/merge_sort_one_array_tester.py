from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.sort.merge_sort.merge_sort import MergeSort
from tech.aelson.algorithms.util.util import Util


def main():
    sortedHalfsOfGrades = [
        Grade("mariana", 5),
        Grade("carlos", 8.5),
        Grade("lucia", 9.3),
        Grade("ana", 10),

        Grade("jonas", 3),
        Grade("andre", 4),
        Grade("juliana", 6.7),
        Grade("guilherme", 7),
        Grade("paulo", 9),
    ]
    unsortedGrades = [
        Grade("mariana", 5),
        Grade("ana", 10),
        Grade("carlos", 8.5),
        Grade("lucia", 9.3),
        Grade("andre", 4),
        Grade("paulo", 9),
        Grade("juliana", 6.7),
        Grade("jonas", 3),
        Grade("guilherme", 7),
    ]
    # Util.print_grades_array("Grades array: ", sortedHalfsOfGrades)
    Util.print_grades_array("Grades array: ", unsortedGrades)

    # rank = MergeSort.sort_one_array_with_two_ordered_halfs(sortedHalfsOfGrades, 0, 4, len(sortedHalfsOfGrades))
    MergeSort.merge_sort(unsortedGrades, 0, len(unsortedGrades))
    Util.print_grades_array("Sorted array: ", unsortedGrades)


if __name__ == "__main__":
    main()

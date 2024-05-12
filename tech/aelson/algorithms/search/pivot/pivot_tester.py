from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.search.pivot.pivot import Pivot
from tech.aelson.algorithms.util.util import Util


def main():
    guilherme = Grade("guilherme", 7)
    unsorted_grades = Util.get_unsorted_grades(guilherme)

    pivot_position = Pivot.execute(unsorted_grades, len(unsorted_grades))
    print("The Pivot is in the position", pivot_position)
    for grade in unsorted_grades:
        print(grade.get_student_name(), grade.get_result())


if __name__ == "__main__":
    main()
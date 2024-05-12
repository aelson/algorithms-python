from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.search.pivot.pivot import Pivot


def main():
    guilherme = Grade("guilherme", 7)
    unsorted_grades = [
        Grade("andre", 4),
        Grade("carlos", 8.5),
        Grade("ana", 10),
        Grade("jonas", 3),
        Grade("juliana", 6.7),
        Grade("lucia", 9.3),
        Grade("paulo", 9),
        Grade("mariana", 5),
        guilherme
    ]

    pivot_position = Pivot.execute(unsorted_grades, 0, len(unsorted_grades))
    print("The Pivot is in the position", pivot_position)
    for grade in unsorted_grades:
        print(grade.get_student_name(), grade.get_result())


if __name__ == "__main__":
    main()
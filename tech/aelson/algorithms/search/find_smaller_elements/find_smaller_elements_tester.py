from tech.aelson.algorithms.search.find_smaller_elements.find_smaller_elements import FindSmallerElements
from tech.aelson.algorithms.model.grade import Grade


def main():
    guilherme = Grade("guilherme", 7)
    unsorted_grades = [
        Grade("andre", 4),
        Grade("carlos", 8.5),
        Grade("ana", 10),
        Grade("jonas", 3),
        Grade("juliana", 6.7),
        guilherme,
        Grade("paulo", 9),
        Grade("mariana", 5),
        Grade("lucia", 9.3),
    ]

    lower_values_count = FindSmallerElements.execute(guilherme, unsorted_grades)
    print("Lower values count:", lower_values_count)


if __name__ == "__main__":
    main()

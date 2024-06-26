from tech.aelson.algorithms.search.find_smaller_elements.find_smaller_elements import FindSmallerElements
from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.util.util import Util


def main():
    guilherme = Grade("guilherme", 7)
    unsorted_grades = Util.get_unsorted_grades(guilherme)

    lower_values_count = FindSmallerElements.execute(guilherme, unsorted_grades)
    print("Lower values count:", lower_values_count)


if __name__ == "__main__":
    main()

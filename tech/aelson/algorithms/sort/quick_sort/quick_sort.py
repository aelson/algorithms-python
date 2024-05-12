from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.search.pivot.pivot import Pivot


class QuickSort:
    @staticmethod
    def execute(grades, start, end):
        print("Executing for", start, "-", end)
        number_of_elements = end - start
        if number_of_elements > 1:
            pivot_index = Pivot.execute(grades, end)
            QuickSort.execute(grades, start, pivot_index)
            QuickSort.execute(grades, pivot_index + 1, end)

from typing import List
from tech.aelson.algorithms.model.grade import Grade
from tech.aelson.algorithms.util.util import Util


class Pivot:
    @staticmethod
    def execute(grades: List[Grade], end: int) -> int:
        pivot = grades[end - 1]
        lower_values_count = 0
        for index in range(0, end - 1):
            current = grades[index]
            if current.get_result() < pivot.get_result():
                if index != lower_values_count:
                    Util.swap(grades, index, lower_values_count)
                lower_values_count += 1
        if end - 1 != lower_values_count:
            Util.swap(grades, end - 1, lower_values_count)
        return lower_values_count

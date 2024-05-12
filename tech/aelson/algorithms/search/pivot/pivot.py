from typing import List
from tech.aelson.algorithms.model.grade import Grade


class Pivot:
    @staticmethod
    def execute(grades: List[Grade], start: int, end: int) -> int:
        pivot = grades[end - 1]
        lower_values_count = 0
        for index in range(start, end - 1):
            current = grades[index]
            if current.get_result() <= pivot.get_result():
                Pivot.swap(grades, index, lower_values_count)
                lower_values_count += 1
        Pivot.swap(grades, end - 1, lower_values_count)
        return lower_values_count

    @staticmethod
    def swap(grades: List[Grade], from_index: int, to_index: int) -> None:
        grade1 = grades[from_index]
        grade2 = grades[to_index]
        grades[to_index] = grade1
        grades[from_index] = grade2

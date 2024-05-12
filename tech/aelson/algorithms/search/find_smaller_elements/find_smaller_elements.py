from typing import List
from tech.aelson.algorithms.model.grade import Grade


class FindSmallerElements:
    @staticmethod
    def execute(reference: Grade, unsorted_grade: List[Grade]) -> int:
        lower_values_count = 0
        for grade in unsorted_grade:
            if grade.get_result() < reference.get_result():
                lower_values_count += 1
        return lower_values_count

from typing import List
from tech.aelson.algorithms.model.grade import Grade


class MergeSort:
    @staticmethod
    def execute(first_array: List[Grade], second_array: List[Grade]) -> List[Grade]:
        total = len(first_array) + len(second_array)
        merged = [None] * total
        current_of_first_array = 0
        current_of_second_array = 0
        current_of_merged = 0

        while current_of_first_array < len(first_array) and current_of_second_array < len(second_array):
            grade1 = first_array[current_of_first_array]
            grade2 = second_array[current_of_second_array]

            print("Comparing", grade1.get_student_name(), "(", grade1.get_result(), ") with", grade2.get_student_name(), "(", grade2.get_result(), ")")

            if grade1.get_result() < grade2.get_result():
                print("-> Inserting", grade1.get_student_name(), "(", grade1.get_result(), ") on the position", current_of_merged)
                merged[current_of_merged] = grade1
                current_of_first_array += 1
            else:
                print("-> Inserting", grade2.get_student_name(), "(", grade2.get_result(), ") on the position", current_of_merged)
                merged[current_of_merged] = grade2
                current_of_second_array += 1

            print("------------------------------------")
            current_of_merged += 1

        while current_of_first_array < len(first_array):
            print("-> Inserting", first_array[current_of_first_array].get_student_name(), "(", first_array[current_of_first_array].get_result(), ") on the position", current_of_merged, "because it is left over from the first array")
            merged[current_of_merged] = first_array[current_of_first_array]
            current_of_first_array += 1
            current_of_merged += 1

        while current_of_second_array < len(second_array):
            print("-> Inserting", second_array[current_of_second_array].get_student_name(), "(", second_array[current_of_second_array].get_result(), ") on the position", current_of_merged, "because it is left over from the second array")
            merged[current_of_merged] = second_array[current_of_second_array]
            current_of_second_array += 1
            current_of_merged += 1

        return merged
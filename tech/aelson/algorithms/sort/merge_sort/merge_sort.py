from typing import List
from tech.aelson.algorithms.model.grade import Grade


class MergeSort:
    @staticmethod
    def merge_two_arrays(first_array: List[Grade], second_array: List[Grade]) -> List[Grade]:
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

    @staticmethod
    def sort_one_array(array: List[Grade], start, middle, end) -> List[Grade]:
        total = len(array)
        sorted_list = []
        sorted_index = 0
        first_part_index = start
        second_part_index = middle

        while first_part_index < middle and second_part_index < end:
            print("Comparing", array[first_part_index].get_student_name(), "(", array[first_part_index].get_result(), ") with",
                  array[second_part_index].get_student_name(), "(", array[second_part_index].get_result(), ")")

            if array[first_part_index].get_result() < array[second_part_index].get_result():
                print("-> Inserting", array[first_part_index].get_student_name(), "(", array[first_part_index].get_result(),
                      ") on the position", sorted_index)
                sorted_list.append(array[first_part_index])
                first_part_index += 1
            else:
                print("-> Inserting", array[second_part_index].get_student_name(), "(", array[second_part_index].get_result(),
                      ") on the position", sorted_index)
                sorted_list.append(array[second_part_index])
                second_part_index += 1

            print("------------------------------------")
            sorted_index += 1

        while first_part_index < middle:
            print("-> Inserting", array[first_part_index].get_student_name(), "(", array[first_part_index].get_result(),
                  ") on the position", sorted_index, "because it is left over from the first part of the array")
            sorted_list.append(array[first_part_index])
            first_part_index += 1
            sorted_index += 1

        while second_part_index < end:
            print("-> Inserting", array[second_part_index].get_student_name(), "(", array[second_part_index].get_result(),
                  ") on the position", sorted_index, "because it is left over from the second part of the array")
            sorted_list.append(array[second_part_index])
            second_part_index += 1
            sorted_index += 1

        if start > 0:
            print("Rebuilding the original array keeping the initial object(s) not ordered "
                  "(because the start is greater then 0)")
            for index_of_merged in range(sorted_index):
                print("-> Inserting", sorted_list[index_of_merged].get_student_name(), "(", sorted_list[index_of_merged].get_result(),
                      ") on the position", start + index_of_merged)
                array[start + index_of_merged] = sorted_list[index_of_merged]

        return array

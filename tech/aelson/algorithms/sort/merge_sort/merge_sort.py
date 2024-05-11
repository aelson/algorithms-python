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

        current_of_merged = MergeSort.add_remaining_elements_to_end_of_array(first_array, len(first_array), current_of_first_array, merged, current_of_merged)
        MergeSort.add_remaining_elements_to_end_of_array(second_array, len(second_array), current_of_second_array, merged, current_of_merged)

        return merged

    @staticmethod
    def sort_one_array(array: List[Grade], start, middle, end) -> List[Grade]:
        total = len(array)
        sorted_list = [None] * total
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

        sorted_index = MergeSort.add_remaining_elements_to_end_of_array(array, middle, first_part_index, sorted_list, sorted_index)
        MergeSort.add_remaining_elements_to_end_of_array(array, end, second_part_index, sorted_list, sorted_index)
        if start + end < len(array):
            MergeSort.rebuild_array(array, start, sorted_index, sorted_list)

        return array

    @staticmethod
    def add_remaining_elements_to_end_of_array(array, array_end, array_index, merged, merged_array_index):
        while array_index < array_end:
            print("-> Inserting", array[array_index].get_student_name(), "(", array[array_index].get_result(), ") on the position", merged_array_index, "because it is left over from the first array")
            merged[merged_array_index] = array[array_index]
            array_index += 1
            merged_array_index += 1
        return merged_array_index

    @staticmethod
    def rebuild_array(array, start, sorted_index, sorted):
        print("Rebuilding the original array")
        for index_of_merged in range(sorted_index):
            print("-> Inserting", sorted[index_of_merged].student_name(), "(", sorted[index_of_merged].result(), ") on the position", index_of_merged)
            array[start + index_of_merged] = sorted[index_of_merged]

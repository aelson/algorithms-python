class Grade:
    def __init__(self, student_name, result):
        self._student_name = student_name
        self._result = result

    def __str__(self):
        return f"{self._student_name}: {self._result}"

    def get_result(self):
        return self._result

    def get_student_name(self):
        return self._student_name

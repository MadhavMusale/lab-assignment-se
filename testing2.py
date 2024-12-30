# Class to capture students' grades
class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student_name, grade):
        if student_name in self.grades:
            self.grades[student_name].append(grade)
        else:
            self.grades[student_name] = [grade]

    def get_grades(self, student_name):
        return self.grades.get(student_name, [])

    def get_average(self, student_name):
        grades = self.grades.get(student_name, [])
        if not grades:
            return 0
        return sum(grades) / len(grades)

# Unit Tests
import unittest

class TestStudentGrades(unittest.TestCase):

    def setUp(self):
        self.student_grades = StudentGrades() 

    def test_add_grade(self):
        self.student_grades.add_grade("Alice", 90)
        self.assertEqual(self.student_grades.get_grades("Alice"), [90])
        self.student_grades.add_grade("Alice", 80)
        self.assertEqual(self.student_grades.get_grades("Alice"), [90, 80])

    def test_get_grades(self):
        self.assertEqual(self.student_grades.get_grades("Bob"), [])  # No grades added yet
        self.student_grades.add_grade("Bob", 70)
        self.assertEqual(self.student_grades.get_grades("Bob"), [70])

    def test_get_average(self):
        self.assertEqual(self.student_grades.get_average("Charlie"), 0)  # No grades
        self.student_grades.add_grade("Charlie", 85)
        self.student_grades.add_grade("Charlie", 75)
        self.assertAlmostEqual(self.student_grades.get_average("Charlie"), 80)

if __name__ == "__main__":
    unittest.main()

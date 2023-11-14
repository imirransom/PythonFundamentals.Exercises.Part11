from enum import Enum
import uuid
class AliveStatus(Enum):
    deceased = 0
    alive = 1

class Person:
    def __init__(self, first_name, last_name, dob, alive=AliveStatus):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self):
        return self.first_name

    def update_last_name(self):
        return self.last_name

    def update_dob(self):
        return self.dob

    def update_status(self):
        return self.alive


class Instructor(Person):
    # def __init__(self, first_name, last_name, dob, alive=AliveStatus):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.dob = dob
    instructor_id = "Instructor_" + str(uuid.uuid4())

    class Student(Person):
        student_id = "Student_" + str(uuid.uuid4())

    class ZipCodeStudent(Student):
        pass

    class CollegeStudent(Student):
        pass

    class Classroom:
        def __init__(self, students: list, instructors: list):
            self.students = students
            self.instructors = instructors
        def add_instructor(self, name):
            return self.instructors.append(name)

        def remove_instructor(self, name):
            return self.instructors.remove(name)

        def add_student(self, name):
            return self.students.append(name)

        def remove_student(self, name):
            return self.students.remove(name)

        def print_instructors(self):
            for instructor in self.instructors:
                print(instructor)

        def print_students(self):
            for student in self.students:
                print(student)


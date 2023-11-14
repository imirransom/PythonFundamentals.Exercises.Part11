from enum import Enum
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
    pass
class Student:

    def __init__(self):
        self.__password = "abc123"

    def show_password(self):
        print(self.__password)

s = Student()

s.show_password()
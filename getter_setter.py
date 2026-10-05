class Student:

    def __init__(self, name, marks):
        self.__name = name        # Private data
        self.__marks = marks      # Private data


    # Getter Method (Read data)
    def get_marks(self):
        return self.__marks


    # Setter Method (Change data)
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully!")
        else:
            print("Invalid Marks!")


    # Getter Method for name
    def get_name(self):
        return self.__name



# Creating Object
student = Student("Ali", 85)


# Using Getter
print("Student Name:", student.get_name())
print("Old Marks:", student.get_marks())


# Using Setter
student.set_marks(95)


# Using Getter again
print("New Marks:", student.get_marks())
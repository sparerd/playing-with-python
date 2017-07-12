students = []


# functions
def print_students(students):
    for student in students:
        print(f"Name: {student['name']}, ID: {student['student_id']}")


# has arguments
def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


# variable arity, saved as list
def var_args(name, *args):
    print(name)
    print(args)


# variable arity, saved as dictionary
def var_args_dict(name, **args):
    print(name)
    print(args)


add_student("Mark", 3915)
add_student(name="Jenny", student_id=5881)
print_students(students)
var_args("Mark", "something", None, True, 124)
var_args_dict("Jenny", description="thingy", age=24)

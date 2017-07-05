# print to console
print("Hello world!")

# types
anInt = 42
aFloat = 4.21
aTypeCastedInt = int(1.234)  # 1
aString = "my string"  # unicode string
aBoolean = True
int(True)  # 1
int(False)  # 0
(3, 5, 1)  # tuple, immutable
set([3, 1, 2])  # unique and ordered (1, 2, 3)
frozenset([3, 1, 2])  # also immutable


# uses type hinting
def add_numbers(a: int, b: int) -> int:
    print(a + b)


# does not use type hinting
def subtract_numbers(a, b):
    print(a - b)

add_numbers(1, 2)
subtract_numbers(1, 1)

# nifty string functions
"hello".capitalize()
"hello".replace("e", "a")
"item1,item2,item3".split(",")

# string interpolation
print(f"this is {aString}. this is a number {anInt}")

# None is the python equivalent of null/nil
aNullVariable = None

thingy = 5
if thingy == 5:
    print("was true")
else:
    print("was false")

# truthy testing. tests that var is assigned, string is not empty, etc
text = "Python"
if thingy:
    print("number is defined")
if text:
    print("text is defined")
if not text:
    print("will not execute since text is defined")

# and/or
if True and False:
    print("will never run")
if True or False:
    print("will always run")

# ternary if statements
a = 1
b = 2
"bigger" if a > b else "smaller"

# lists
names = []  # empty list
names = ["jane", "john", "mark"]
names[0]   # jane
names[-1]  # mark
names[-2]  # john
names[0] = "James"  # replace jane with james
names.append("Jessica")  # add Jessica to end of list
del names[3]  # removed Jessica
"john" in names  # true
len(names)  # 3
names[1:]  # john, mark (list slicing, unbounded)
names[1:2]  # john, mark (list slicing, bounded)

# loops
# python version of foreach
for name in names:
    print(f"Name is {name}")

x = 0
for index in range(10):
    x += 10
    print(f"X = {x}")

# range
range(10)
range(5, 10)  # 5, 6, 7, 8, 9, 10
range(5, 10, 2)  # 5, 7, 9

# loop breaking
for name in names:
    if name == "john":
        print("found john")
        break
    print("testing" + name)

# loop continue
for name in names:
    if name == "jane":
        continue
    print(name)

# while loop
x = 0
while x < 10:
    print(x)
    x += 1

# dictionaries
student = {
    "name": "Mark",
    "student_id": 15128,
    "feedback": None
}

student["name"]
student["student_id"]
# student["last_name"]  # would throw an error
student["name"] = "James"

# exceptions
try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding last_name")
except Exception:
    print("Unknown error")
finally:
    print("finally ran")

# capture error
try:
    unsupported_error = 3 + ""
except TypeError as error:
    print(error)

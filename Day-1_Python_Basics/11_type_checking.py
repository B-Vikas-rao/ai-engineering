# Type Checking in Python

name = "Vikas"
age = 20
cgpa = 8.5
is_student = True

# Using type()
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

# Using isinstance()
print(isinstance(name, str))
print(isinstance(age, int))
print(isinstance(cgpa, float))
print(isinstance(is_student, bool))

# Output:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# True
# True
# True
# True
#*args - to accept unlimited argument
def total(*numbers):
    return sum(numbers)

# print(total(3,6,3,2,7))
#  **Kwargs - to accept unlimited named arguments
def show_info(**details):
    for key , value in details.items():
        print(f"{key}: {value}")

# show_info(name= "Bereket" , age=20 , country="Ethiopia")
 
    # 3) List comprehension 
numbers = [2,4,7,2,9,0,6]
square=[]
[square.append(n*n) for n in numbers if n%2 == 0] 
# print(square)

#  part 3 Dictionary

student = {"name":"ashenafi" , "age":22 , "level": "3rd year ingineering student"}
student["level"]="2nd level"
print(student["name"])
print(student.get("level","not found"))
print(student.get("age","not found"))

#   4 error handling
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"

# print(divide(10, 2))     
# print(divide(10, 0))    
# print(divide(10, "a"))    

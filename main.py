print ("""     _______________
          |               |
          |     CLI       |
          |               |
          |_______________|""")

print("Welcome to the CLI tool!")
students = []
num_students = int(input("how many student do you want to enter?:"))
i = 0
while i < num_students:
    print(f"Enter details for student {i + 1}:")
    # Add code here to collect student details
    name = input("Enter name: ")
    age = int(input("Enter age: "))  
    sex = input("Enter sex: ")
    score = float(input("Enter score : "))  
    status = "darbee" if score >= 50 else "hin darbine"
    student = {
        "ID": i + 1,    
        "name": name,
        "age": age,
        "sex": sex, 
        "score": score,
        "status": status
    }
    students.append(student)
    i += 1
    print("\n Student details added successfully!\n")

print("\nAll student details:")
for student in students:
    print(f""" ID: {student['ID']}, Name: {student['name']},
          Age: {student['age']}, Sex: {student['sex']}, 
          Score: {student['score']}, Status: {student['status'] } """)      
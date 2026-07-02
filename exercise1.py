# Build a function called analyze_students that:

# Accepts *students — unlimited number of dictionaries, each with name and score
# Returns a list of names of students who scored 50 or above — using list comprehension
# If any student dictionary is missing the score key, catch the error and skip that student instead of crashing

def analyze_students(*students):
    passed = [
       student.get("name","unkonwn")
       for student in students
       if student.get("score")>=50
    ]       
    return passed   
result = analyze_students(
    {"name":"beki","level":"2nd" ,"score" :100},
    { "name":"abel" ,"level":"3rd","score":98},
    {"name":"ashu","level":"4th" , "score":34}
            )
    
print("passed student", result)
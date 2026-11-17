students = {} 
 
def calculate_grade(marks):     
    if marks >= 90:         
        return "A+"     
    elif marks >= 80:         
        return "A"    
    elif marks >= 70:         
        return "B"     
    elif marks >= 60:         
        return "C"     
    elif marks >= 50:        
         return "D"     
    else: 
        return "F" 
 
n = int(input("Enter number of students: ")) 
 
for i in range(n): 
    name = input("\nEnter student name: ")     
    marks = float(input("Enter marks out of 100: ")) 
 
    if marks < 0 or marks > 100: 
        print("Invalid marks! Enter marks between 0 and 100.")         
        continue 
 
    students[name] = marks 
 
print("\n--- STUDENT RESULTS ---") 
 
for name, marks in students.items():     
    grade = calculate_grade(marks) 
 
    print("Name:", name)     
    print("Marks:", marks)     
    print("Grade:", grade)     
    print("-------------------") 

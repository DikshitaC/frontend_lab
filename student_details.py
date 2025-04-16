def student_details():
    students = []
    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter name: ")
        roll_no = input("Enter roll number: ")
        department = input("Enter department: ")
        address = input("Enter address: ")
        gender = input("Enter gender: ")
        marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
        total_marks = sum(marks)
        percentage = total_marks / 3
        students.append({'name': name, 'marks': marks, 'total': total_marks, 'percentage': percentage})
    
    max_marks_student = max(students, key=lambda x: x['total'])
    min_marks_student = min(students, key=lambda x: x['total'])
    fail_students = [s['name'] for s in students if min(s['marks']) < 10]
    
    print("Student Details:")
    for student in students:
        print(student)
    print(f"Student with max marks: {max_marks_student['name']}")
    print(f"Student with min marks: {min_marks_student['name']}")
    print(f"Failing students: {fail_students}")

student_details()

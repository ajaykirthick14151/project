n = int(input("Enter number of students: "))

for i in range(n):

    print("\n--- Student", i + 1, "---")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    print("Enter marks for 5 subjects:")

    m1 = float(input("Subject 1: "))
    m2 = float(input("Subject 2: "))
    m3 = float(input("Subject 3: "))
    m4 = float(input("Subject 4: "))
    m5 = float(input("Subject 5: "))

    total = m1 + m2 + m3 + m4 + m5
    average = total / 5

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n===== RESULT REPORT =====")
    print("Name    :", name)
    print("Roll No :", roll_no)
    print("Total   :", total)
    print("Average :", average)
    print("Grade   :", grade)
    print("Result  :", result)
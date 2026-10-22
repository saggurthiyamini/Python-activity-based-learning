# Case Study 42: Student Marks Matrix Analysis

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Number of students and subjects must be positive.")
else:
    matrix = []
    for i in range(students):
        row = []
        print(f"Enter marks for student {i + 1}:")
        for j in range(subjects):
            row.append(float(input(f"Subject {j + 1}: ")))
        matrix.append(row)

    print("\n--- Student Totals and Averages ---")
    totals = []
    for i, row in enumerate(matrix):
        total = sum(row)
        totals.append(total)
        print(f"Student {i + 1}: total = {total:.2f}, average = {total / subjects:.2f}")

    top_index = totals.index(max(totals))
    print("Top performer: Student", top_index + 1, "with total", totals[top_index])

    print("\n--- Subject Averages ---")
    for j in range(subjects):
        column_total = sum(matrix[i][j] for i in range(students))
        average = column_total / students
        print(f"Subject {j + 1}: average = {average:.2f}")

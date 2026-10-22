# Case Study 11: Examination Result and Grace-Mark Validation

marks = []
subjects = int(input("Enter number of subjects: "))
maximum_marks = int(input("Enter maximum marks per subject: "))
pass_mark = int(input("Enter minimum pass mark per subject: "))
grace_limit = int(input("Enter maximum grace marks allowed per subject: "))

for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    while mark < 0 or mark > maximum_marks:
        print(f"Marks must be between 0 and {maximum_marks}.")
        mark = int(input(f"Re-enter marks for subject {i + 1}: "))
    marks.append(mark)

final_marks = []
grace_used = []

for mark in marks:
    if mark < pass_mark and pass_mark - mark <= grace_limit:
        final_marks.append(pass_mark)
        grace_used.append(pass_mark - mark)
    else:
        final_marks.append(mark)
        grace_used.append(0)

total = sum(final_marks)
percentage = total / (subjects * maximum_marks) * 100
passed = all(mark >= pass_mark for mark in final_marks)

print("\n--- Examination Result ---")
for i in range(subjects):
    print(f"Subject {i + 1}: Original = {marks[i]}, Final = {final_marks[i]}, Grace = {grace_used[i]}")
print("Total marks:", total)
print(f"Percentage: {percentage:.2f}%")
print("Result:", "PASS" if passed else "FAIL")

if passed:
    if percentage >= 75:
        print("Classification: Distinction")
    elif percentage >= 60:
        print("Classification: First Class")
    elif percentage >= 50:
        print("Classification: Second Class")
    else:
        print("Classification: Pass Class")
else:
    print("Classification: Not Classified")

# Case Study 17: Student Performance Trend Analysis

subjects = input("Enter subject names separated by commas: ").split(",")
subjects = [subject.strip() for subject in subjects if subject.strip()]

if not subjects:
    print("Please enter at least one subject.")
else:
    previous = []
    current = []

    print("Enter previous exam marks:")
    for subject in subjects:
        previous.append(float(input(f"{subject}: ")))

    print("Enter current exam marks:")
    for subject in subjects:
        current.append(float(input(f"{subject}: ")))

    print("\n--- Performance Trend ---")
    for i, subject in enumerate(subjects):
        change = current[i] - previous[i]
        if change > 0:
            status = "Improved"
        elif change < 0:
            status = "Declined"
        else:
            status = "No change"
        print(f"{subject}: {previous[i]:.1f} -> {current[i]:.1f}; change = {change:+.1f} ({status})")

    weak_subjects = [subjects[i] for i in range(len(subjects)) if current[i] < 40]
    print("Average previous marks:", round(sum(previous) / len(previous), 2))
    print("Average current marks:", round(sum(current) / len(current), 2))
    print("Subjects below 40 marks:", ", ".join(weak_subjects) if weak_subjects else "None")

    average = sum(current) / len(current)
    if average >= 75:
        print("Overall classification: Excellent")
    elif average >= 60:
        print("Overall classification: Good")
    elif average >= 40:
        print("Overall classification: Satisfactory")
    else:
        print("Overall classification: Needs improvement")

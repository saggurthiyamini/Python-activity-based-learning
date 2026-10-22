# Case Study 12: Attendance Recovery Computation

attended = int(input("Enter classes attended so far: "))
conducted = int(input("Enter total classes conducted so far: "))
target = float(input("Enter required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance data.")
elif target <= 0 or target > 100:
    print("Target must be greater than 0 and at most 100.")
else:
    current = attended / conducted * 100
    print(f"Current attendance: {current:.2f}%")

    if current >= target:
        print("You already meet the attendance requirement.")
    else:
        # Find the minimum consecutive classes that must be attended.
        needed = 0
        while (attended + needed) / (conducted + needed) * 100 < target:
            needed += 1
        print("Minimum consecutive classes to attend:", needed)
        print(f"Attendance after attending them: {(attended + needed) / (conducted + needed) * 100:.2f}%")

# Case Study 21: Traffic Violation Penalty Calculator

fine_rules = {
    "speeding": 1000,
    "no_helmet": 500,
    "signal_jump": 1500,
    "no_seatbelt": 500
}

vehicle = input("Enter vehicle category (two_wheeler/car/heavy): ").strip().lower()
count = int(input("Enter number of violations: "))
total_fine = 0
disqualified = False

for i in range(count):
    offence = input(f"Enter offence {i + 1} (speeding/no_helmet/signal_jump/no_seatbelt): ").strip().lower()
    repeat = input("Is this a repeat offence? (yes/no): ").strip().lower()

    if offence not in fine_rules:
        print("Unknown offence; no fine calculated for this entry.")
        continue

    fine = fine_rules[offence]
    if repeat == "yes":
        fine *= 2

    if vehicle == "heavy":
        fine += 500

    total_fine += fine
    print(f"Fine for this offence: Rs. {fine}")

    if offence == "signal_jump" and repeat == "yes":
        disqualified = True

print("\nTotal penalty: Rs.", total_fine)
print("Disqualification condition:", "Flagged for review" if disqualified else "Not triggered")
print("Note: Fine amounts are illustrative for this programming exercise.")

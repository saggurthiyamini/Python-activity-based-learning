# Case Study 13: ATM Transaction Sequence Simulation

balance = float(input("Enter opening balance: "))
transaction_count = int(input("How many transactions? "))
withdrawal_limit = float(input("Enter maximum allowed withdrawal per transaction: "))

deposits = 0.0
withdrawals = 0.0
accepted = 0
rejected = 0

for i in range(transaction_count):
    print(f"\nTransaction {i + 1}")
    kind = input("Enter D for deposit or W for withdrawal: ").strip().upper()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Rejected: amount must be positive.")
        rejected += 1
    elif kind == "D":
        balance += amount
        deposits += amount
        accepted += 1
        print("Deposit accepted.")
    elif kind == "W":
        if amount > withdrawal_limit:
            print("Rejected: withdrawal limit exceeded.")
            rejected += 1
        elif amount > balance:
            print("Rejected: insufficient balance.")
            rejected += 1
        else:
            balance -= amount
            withdrawals += amount
            accepted += 1
            print("Withdrawal accepted.")
    else:
        print("Rejected: invalid transaction type.")
        rejected += 1

print("\n--- Transaction Summary ---")
print(f"Total deposits: {deposits:.2f}")
print(f"Total withdrawals: {withdrawals:.2f}")
print(f"Accepted transactions: {accepted}")
print(f"Rejected transactions: {rejected}")
print(f"Closing balance: {balance:.2f}")

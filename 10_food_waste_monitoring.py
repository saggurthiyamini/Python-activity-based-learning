# Case Study 53: Food Waste Monitoring System

days = int(input("Enter number of days to monitor: "))
limit = float(input("Enter acceptable wastage percentage: "))

if days <= 0 or limit < 0 or limit > 100:
    print("Invalid number of days or wastage limit.")
else:
    total_prepared = 0
    total_served = 0
    total_leftover = 0
    daily_rates = []

    for day in range(1, days + 1):
        print(f"\nDay {day}")
        prepared = int(input("Meals prepared: "))
        served = int(input("Meals served: "))

        if prepared < 0 or served < 0 or served > prepared:
            print("Invalid data. Meals must be non-negative and served cannot exceed prepared.")
            leftover = 0
            rate = 0
        else:
            leftover = prepared - served
            rate = leftover / prepared * 100 if prepared > 0 else 0

        total_prepared += prepared
        total_served += served
        total_leftover += leftover
        daily_rates.append(rate)

        print(f"Leftover meals: {leftover}")
        print(f"Wastage percentage: {rate:.2f}%")
        if rate > limit:
            print("Warning: Wastage exceeded the acceptable limit.")

    overall_rate = total_leftover / total_prepared * 100 if total_prepared > 0 else 0
    print("\n--- Monitoring Summary ---")
    print("Total meals prepared:", total_prepared)
    print("Total meals served:", total_served)
    print("Total leftovers:", total_leftover)
    print(f"Overall wastage: {overall_rate:.2f}%")
    if daily_rates:
        worst_day = daily_rates.index(max(daily_rates)) + 1
        print("Highest wastage percentage was on day", worst_day)

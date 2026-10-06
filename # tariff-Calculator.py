

def calculate_bill(units):
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

    return bill



units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    bill = calculate_bill(units)

    print("\n----- Electricity Bill -----")
    print(f"Units Consumed : {units:.2f} kWh")
    print(f"Electricity Bill: ₹{bill:.2f}")
    print("----------------------------")

def calculate_bill(cups, price_per_cup):
    return (cups * price_per_cup)

total_bill = calculate_bill(3, 15)
print(total_bill)

print(f"Order for table 2: {calculate_bill(3, 50)}")
names = ["mayank", "meera", "sam", "ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid ₹{amount}")

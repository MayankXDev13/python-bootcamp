# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# value = 13

# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")
    
# available_sizes = ["small", "medium", "large"]

# if (requested_sizes := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_sizes} chai")
# else:
#     print(f"Size is unavailable - {requested_sizes}")
    
    
flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavours)

while (flavour := input("Choose your flavor: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")
    
print(f"You choose {flavour} chai")

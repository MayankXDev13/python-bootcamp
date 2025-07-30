class Chai:
    temperature = "hot"
    strength = "Strong"
    
cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print(f"After changing {cutting.temperature}")
print(f"cup size is {cutting.cup}")
print(f"Direct look into the class {Chai.temperature}")


del cutting.temperature
# del cutting.cup


print(cutting.temperature)
print(cutting.cup)
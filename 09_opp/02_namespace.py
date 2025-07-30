class Chai:
    origin = "India" # this called properties
    
print(Chai.origin)

# add new porperties to chai class
Chai.is_hot = True

print(Chai.is_hot)

# creating objects from class chai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")


masala.is_hot = False
print(f"Class: {Chai.is_hot}")
print(f"Masala {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)
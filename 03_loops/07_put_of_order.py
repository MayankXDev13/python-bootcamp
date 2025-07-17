flavours = ["Ginger", "Out os Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out os Stock":
        continue
    elif flavour == "Discontinued":
        print(f'{flavour} item found')
        break
    print(f'{flavour} item found')
    
print('Out side of loop')
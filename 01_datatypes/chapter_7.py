masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is Ginger : {ginger_ratio} and {cadramom_ratio}")

# swapping var
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio

print(f"Ratio is Ginger : {ginger_ratio} and {cadramom_ratio}")

# membership

print(f"Is ginger in masala spices ? {"Cinnamon" in masala_spices}")
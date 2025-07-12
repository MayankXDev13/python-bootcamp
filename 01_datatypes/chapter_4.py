is_boilig = True
stri_cont = 5
total_action = stri_cont + is_boilig # upcasting
print(f"Total actions: {total_action}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")


water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")
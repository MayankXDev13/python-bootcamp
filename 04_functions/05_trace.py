def add_vat(price, vat_rate):
    return (price + (price / 100) * vat_rate)
    
orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")
items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
]

affordable = [item["name"] for item in items if item["price"] < 500]
categories = {item["category"] for item in items}
price_map = {item["name"]: item["price"]  for item in items }
discounted_prices = list((int(item["price"] * 0.9) for item in items))

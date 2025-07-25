def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")

def chai_counter():
    chai_order = "lemon" # Enclosing scope 
    def print_order():
        chai_order = "Ginger"
        print(f"Inner: {chai_order}")
    print_order()
    print(f"Outer: {chai_order}")
    
chai_order = "Tulsi" # Global
chai_counter()
print(f"Global : {chai_order}")
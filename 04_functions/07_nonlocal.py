def update_order():
    chai_type = "Elaichi"
    def kithcen():
        nonlocal chai_type 
        chai_type = "Kesar"
    kithcen()
    print(f"After kitchen update {chai_type}")

update_order()
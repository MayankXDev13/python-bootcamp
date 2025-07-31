class InvalidChaiError(Exception): pass


def bill(falvor, cups):
    menu = {"masla": 20, "ginger": 40}
    try:
        if falvor not in menu:
            raise InvalidChaiError("that chai is not availble")
        if not isinstance(cups, int):
            raise TypeError("Number of cups of be an integer")
        total = menu["flavor"] * cups        
        print(f"Your bill for {cups} cups of {falvor} chaiL rupees {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally: 
        print("Thank you for visiting chaicode!")
        
bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
class OutOfIngrediwntsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngrediwntsError("Missing milk or sugar")
    print("chai is readyf")
    
make_chai(0, 1)
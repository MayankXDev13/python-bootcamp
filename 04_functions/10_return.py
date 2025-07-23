# def make_chai():
#     return "Here is your masal chia"
#     print("Here is your masala chai")

# return_value = make_chai()
# print(return_value)


def idle_chaiwala():
    pass

print(idle_chaiwala())

def solf_cups():
    return 120

total = solf_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))


def chai_report():
    return 100, 20, 10 #solf, remaining, not_paid

sold, remaining, not_paid = chai_report()
print(f"Sold: {sold}, Remaining: {remaining}")
# nums = [1, 2, 3, 4, 5, 6]
# sq = [num * num for num in nums]
# print(sq)


# words = ['hello', 'world', 'python']
# upper = [word.upper() for word in words]
# print(upper)


# words = ['apple', 'bat', 'cat', 'pineapple']
# word_shorter_than_five = [word for word in words if len(word) < 5] 
# print(word_shorter_than_five)


# matrix = [[1, 2], [3, 4], [5, 6]]
# flatten = [list for lists in matrix for list in lists]
# print(flatten)

a = [1, 2]
b = [10, 20]
products = [x*y for x in a for y in b]
print(products)
def linear_search(items, target):
    for index in range(len(items)):
        if items[index] == target:
            return index
    return -1

numbers = [4,6,8,10,23,16,32]
print(linear_search(numbers,16))
print(linear_search(numbers, 100))
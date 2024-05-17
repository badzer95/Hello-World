def BinarySearch(lst:list, num:int) -> int:
    min = 0
    max = len(lst) - 1
    while min <= max:
        index = (max + min) // 2
        if num > lst[index]:
            min = index + 1
        elif num < lst[index]:
            max = index - 1
        elif num == lst[index]:
            return index
    return None

lst = [2, 3, 4, 9, 18, 39, 40, 55, 69, 71, 75, 77, 85, 90, 95, 96, 97]
print(len(lst))

print(BinarySearch(lst, 39))
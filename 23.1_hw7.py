from random import sample, randint


def binary_search(list1, number):
    first = 0
    last = len(list1) - 1
    result = 'false'
    position = 0

    while first <= last:
        middle = (first + last) // 2
        if list1[middle] == number:
            first = middle
            last = first
            result = 'true'
            position = list1[middle]
            break
        else:
            if list1[middle] > number:
                last = middle - 1
            else:
                first = middle + 1
    if result == 'true':
        return f'{position} exists'
    else:
        return f'does not exist'


list2 = list(sample(range(0, 11), 5))
list2.sort()
print(f'list {list2}')
number1 = randint(1, 5)
print(f'number {number1}')
print(binary_search(list2, number1))


def bubble_sort(list3):
    len1 = len(list3) - 1
    while len1 > 0:
        for i in range(len1):
            if list3[i] > list3[i + 1]:
                list3[i], list3[i + 1] = list3[i + 1], list3[i]
        len1 -= 1
    return list3


nums = sample(range(1, 10), 5)
print(nums)
print(bubble_sort(nums))


def selection_sort(list3):
    len1 = len(list3) - 1
    while len1 > 0:
        for i in range(len1):
            if list3[i] < list3[len1]:
                list3[i], list3[len1] = list3[len1], list3[i]
        len1 -= 1
    return list3


nums = sample(range(1, 10), 5)
print(nums)
print(selection_sort(nums))

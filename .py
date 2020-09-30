import random

my_array = [0] * 100

for number in range(len(my_array)):
    my_array[number] = random.randint(1, 1000)


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()

        values_lower = []
        values_greater = []

        for i in array:
            if i < pivot:
                values_lower.append(i)
            else:
                values_greater.append(i)
        return quick_sort(values_lower) + [pivot] + quick_sort(values_greater)


sorted_array = quick_sort(my_array)
print(sorted_array)

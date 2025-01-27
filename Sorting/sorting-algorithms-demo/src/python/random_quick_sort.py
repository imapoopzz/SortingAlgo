def random_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less_than_pivot = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        greater_than_pivot = [x for x in arr if x > pivot]
        return random_quick_sort(less_than_pivot) + equal_to_pivot + random_quick_sort(greater_than_pivot)
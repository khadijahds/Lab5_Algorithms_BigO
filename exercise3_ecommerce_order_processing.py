# Exercise 3: E-Commerce Order Processing

# Student-specific inputs
LAST_NAME = "De Silva"
STUDENT_ID = "TUPM-26-4309"
FAVORITE_ARTIST = "Taylor Swift"

SEED_DIGIT = 9
ID_SUM = 24
NAME_LENGTH = 7
ARTIST_LENGTH = 11
ARTIST_SUM = 168

# Generate 100 unique order values
n = 100

orders = [
    (i * ARTIST_SUM + ID_SUM + SEED_DIGIT) % 10000
    for i in range(n)
]

# Remove duplicates while preserving order
orders = list(dict.fromkeys(orders))

print("=== E-Commerce Order Processing ===")
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")

print("\nOriginal Orders:")
print(orders)

# Create three input arrangements
sorted_orders = sorted(orders)
reverse_orders = sorted(orders, reverse=True)

import random

random_orders = orders.copy()
random.seed(SEED_DIGIT)
random.shuffle(random_orders)

print("\n=== Input Arrangements ===")
print("Sorted Orders:")
print(sorted_orders)

print("\nReverse Orders:")
print(reverse_orders)

print("\nRandom Orders:")
print(random_orders)

# Bubble Sort
def bubble_sort(data):
    arr = data.copy()
    comparisons = 0

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr, comparisons


# Selection Sort
def selection_sort(data):
    arr = data.copy()
    comparisons = 0

    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr, comparisons


# Insertion Sort
def insertion_sort(data):
    arr = data.copy()
    comparisons = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons

# Test all sorting algorithms
datasets = {
    "Sorted": sorted_orders,
    "Reverse": reverse_orders,
    "Random": random_orders
}

print("\n=== Sorting Results ===")

for name, data in datasets.items():
    print(f"\n--- {name} Orders ---")

    bubble_result, bubble_comparisons = bubble_sort(data)
    selection_result, selection_comparisons = selection_sort(data)
    insertion_result, insertion_comparisons = insertion_sort(data)

    print(f"Bubble Sort Comparisons: {bubble_comparisons}")
    print(f"Selection Sort Comparisons: {selection_comparisons}")
    print(f"Insertion Sort Comparisons: {insertion_comparisons}")

    print(f"Bubble Sort Correct: {bubble_result == sorted_orders}")
    print(f"Selection Sort Correct: {selection_result == sorted_orders}")
    print(f"Insertion Sort Correct: {insertion_result == sorted_orders}")
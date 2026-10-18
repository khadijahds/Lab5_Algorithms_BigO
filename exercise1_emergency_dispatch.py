# Exercise 1: Emergency Dispatch Record Search

# Student-specific inputs
LAST_NAME = "De Silva"
STUDENT_ID = "TUPM-26-4309"
FAVORITE_ARTIST = "Taylor Swift"

# Generated values
SEED_DIGIT = 9
ID_SUM = 24
NAME_LENGTH = 7
ARTIST_LENGTH = 11
ARTIST_SUM = 168

# Generate unique incident records
n = 100
original_data = [
    (i * ARTIST_SUM + ID_SUM) % 10000
    for i in range(n)
]

# Make sure the values are unique
original_data = list(dict.fromkeys(original_data))

# Rotation using SEED_DIGIT
rotation = SEED_DIGIT
rotated_data = original_data[rotation:] + original_data[:rotation]

# Generate target incident
target = original_data[(ID_SUM + ARTIST_SUM) % len(original_data)]

print("=== Emergency Dispatch Record Search ===")
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")
print(f"SEED_DIGIT: {SEED_DIGIT}")
print(f"ID_SUM: {ID_SUM}")
print(f"ARTIST_SUM: {ARTIST_SUM}")

print("\nOriginal Dataset:")
print(original_data)

print("\nRotated Dataset:")
print(rotated_data)

print(f"\nTarget Incident: {target}")

# Linear Search
def linear_search(data, target):
    comparisons = 0

    for i, value in enumerate(data):
        comparisons += 1

        if value == target:
            return i, comparisons

    return -1, comparisons


linear_position, linear_comparisons = linear_search(rotated_data, target)

print("\n=== Linear Search ===")
print(f"Target: {target}")
print(f"Position: {linear_position}")
print(f"Comparisons: {linear_comparisons}")

# Binary Search
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if data[mid] == target:
            return mid, comparisons
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Binary Search requires sorted data
sorted_data = sorted(rotated_data)

binary_position, binary_comparisons = binary_search(sorted_data, target)

print("\n=== Binary Search ===")
print(f"Target: {target}")
print(f"Position: {binary_position}")
print(f"Comparisons: {binary_comparisons}")

# Complexity Analysis

print("\n=== Complexity Analysis ===")
print("Linear Search - Time Complexity: O(n)")
print("Linear Search - Space Complexity: O(1)")
print("Binary Search - Time Complexity: O(log n)")
print("Binary Search - Space Complexity: O(1)")
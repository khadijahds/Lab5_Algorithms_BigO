# Exercise 2: University Enrollment Records

# Student-specific inputs
LAST_NAME = "De Silva"
STUDENT_ID = "TUPM-26-4309"
FAVORITE_ARTIST = "Taylor Swift"

SEED_DIGIT = 9
ID_SUM = 24
NAME_LENGTH = 7
ARTIST_LENGTH = 11
ARTIST_SUM = 168

# Generate Department A records
department_a = [
    (i * ID_SUM + NAME_LENGTH) % 1000
    for i in range(50)
]

# Generate Department B records
department_b = [
    (i * ARTIST_SUM + SEED_DIGIT) % 1000
    for i in range(50)
]

# Remove duplicates while keeping the order
department_a = list(dict.fromkeys(department_a))
department_b = list(dict.fromkeys(department_b))

# Consolidate the two departments
consolidated = department_a + department_b

print("=== University Enrollment Records ===")
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")

print("\nDepartment A:")
print(department_a)

print("\nDepartment B:")
print(department_b)

print("\nConsolidated Records:")
print(consolidated)

# Insertion Sort with comparison counting
sorted_consolidated = consolidated.copy()
comparisons = 0

for i in range(1, len(sorted_consolidated)):
    key = sorted_consolidated[i]
    j = i - 1

    while j >= 0:
        comparisons += 1

        if sorted_consolidated[j] > key:
            sorted_consolidated[j + 1] = sorted_consolidated[j]
            j -= 1
        else:
            break

    sorted_consolidated[j + 1] = key

# Verify ordering
is_sorted = all(
    sorted_consolidated[i] <= sorted_consolidated[i + 1]
    for i in range(len(sorted_consolidated) - 1)
)

print("\n=== Analysis ===")
print(f"Original consolidated records: {len(consolidated)}")
print(f"Comparisons: {comparisons}")
print(f"Sorted records: {sorted_consolidated}")

is_sorted = all(
    sorted_consolidated[i] <= sorted_consolidated[i + 1]
    for i in range(len(sorted_consolidated) - 1)
)

print(f"Records are sorted: {is_sorted}")

print("\n=== Complexity Analysis ===")
print("Insertion Sort Time Complexity: O(n²)")
print("Insertion Sort Space Complexity: O(1)")
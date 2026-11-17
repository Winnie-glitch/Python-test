students = {}  # Start with an empty dictionary

# Loop 3 times to collect name and score
for _ in range(3):
    name = input("Enter student name: ")  # e.g., "John"
    score = int(input("Enter score: "))   # e.g., 85
    students[name] = score  # Store in dictionary

# Find the student with the highest score
top_student = max(students, key=students.get)

print("Top student:", top_student)


def sum_of_digits(num: int) -> int:
    return sum(int(digit) for digit in str(num))
print(sum_of_digits(11223344556678899900))
def sum_of_digits(nums) -> list:
    # If only one number is given (not a list), make it a list
    if isinstance(nums, int):
        nums = [nums]

    results = []
    for num in nums:
        digit_sum = sum(int(digit) for digit in str(num))
        results.append(digit_sum)

    return results

# Example with multiple numbers
print(sum_of_digits([11, 22, 33, 44, 55]))  # [2, 4, 6, 8, 10]

# Example with single number
print(sum_of_digits(1234))  # [10]

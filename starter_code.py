"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """
    if len(numbers) == 0:
        return 0

    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])

    return count_even(numbers[1:])


def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings) == 0:
        return []

    if target in strings[0]:
        return [strings[0]] + find_strings_with(strings[1:], target)

    return find_strings_with(strings[1:], target)


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    """

    # Base case: if the path is a file, count it as 1
    if os.path.isfile(directory_path):
        return 1

    # Recursive case: directory
    total = 0

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            total += 1

        elif os.path.isdir(full_path):
            total += count_files(full_path)

    return total


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    Returns a list of full paths to infected files.
    """

    # Base case: if this is a file, check its extension
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        else:
            return []

    # Recursive case: directory
    infected_files = []

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            if full_path.endswith(extension):
                infected_files.append(full_path)

        elif os.path.isdir(full_path):
            infected_files.extend(
                find_infected_files(full_path, extension)
            )

    return infected_files


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":

    print("RECURSION ASSIGNMENT")
    print("====================\n")

    # ------------------------------------------------------------------------
    # PART 1 TESTS
    # ------------------------------------------------------------------------

    print("Test sum_list:")
    print(
        f"  sum_list([1, 2, 3, 4]) = "
        f"{sum_list([1, 2, 3, 4])} (expected: 10)"
    )

    print(
        f"  sum_list([]) = "
        f"{sum_list([])} (expected: 0)"
    )

    print(
        f"  sum_list([5, 5, 5]) = "
        f"{sum_list([5, 5, 5])} (expected: 15)"
    )

    print("\nTest count_even:")
    print(
        f"  count_even([1, 2, 3, 4, 5, 6]) = "
        f"{count_even([1, 2, 3, 4, 5, 6])} (expected: 3)"
    )

    print(
        f"  count_even([1, 3, 5]) = "
        f"{count_even([1, 3, 5])} (expected: 0)"
    )

    print(
        f"  count_even([2, 4, 6]) = "
        f"{count_even([2, 4, 6])} (expected: 3)"
    )

    print("\nTest find_strings_with:")

    result = find_strings_with(
        ["hello", "world", "help", "test"],
        "hel"
    )

    print(
        f"  Result: {result}"
        f" (expected: ['hello', 'help'])"
    )

    result = find_strings_with(
        ["cat", "dog", "bird"],
        "z"
    )

    print(
        f"  Result: {result}"
        f" (expected: [])"
    )


    # ------------------------------------------------------------------------
    # PART 2: COUNT FILES TESTS
    # ------------------------------------------------------------------------

    print("\nTest count_files:")

    print(
        "  Total files (Test Case 1):",
        count_files("test_cases/case1_flat"),
        "(expected: 5)"
    )

    print(
        "  Total files (Test Case 2):",
        count_files("test_cases/case2_nested"),
        "(expected: 4)"
    )

    print(
        "  Total files (Test Case 3):",
        count_files("test_cases/case3_infected"),
        "(expected: 5)"
    )


    # ------------------------------------------------------------------------
    # PART 2: BREACH DATA
    # ------------------------------------------------------------------------

    print("\nBreach Data:")

    total_files = count_files("breach_data")

    print(
        "  Total files in breach_data:",
        total_files
    )


    # ------------------------------------------------------------------------
    # PART 3: FIND INFECTED FILES TESTS
    # ------------------------------------------------------------------------

    print("\nTest find_infected_files:")

    infected_case1 = find_infected_files(
        "test_cases/case1_flat"
    )

    print(
        "  Test Case 1 infected files:",
        len(infected_case1),
        "(expected: 0)"
    )

    infected_case2 = find_infected_files(
        "test_cases/case2_nested"
    )

    print(
        "  Test Case 2 infected files:",
        len(infected_case2),
        "(expected: 0)"
    )

    infected_case3 = find_infected_files(
        "test_cases/case3_infected"
    )

    print(
        "  Test Case 3 infected files:",
        len(infected_case3),
        "(expected: 3)"
    )


    # ------------------------------------------------------------------------
    # PART 3: FIND ALL INFECTED FILES
    # ------------------------------------------------------------------------

    print("\nBreach Analysis:")

    infected_files = find_infected_files(
        "breach_data"
    )

    print(
        "  Total infected files:",
        len(infected_files)
    )

    print("\n  Infected file paths:")

    for file_path in infected_files:
        print("   ", file_path)


    # ------------------------------------------------------------------------
    # DEPARTMENT ANALYSIS
    # ------------------------------------------------------------------------

    print("\nDepartment Analysis:")
finance_files = find_infected_files(
    "breach_data/Finance"
)

marketing_files = find_infected_files(
    "breach_data/Marketing"
)

print(
    "  Finance infected files:",
    len(finance_files)
)

print(
    "  Marketing infected files:",
    len(marketing_files)
)
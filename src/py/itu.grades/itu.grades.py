from itu.algs4.sorting import insertion_sort

"""
This submission uses library from ITU specific for course Algorithms and
data structures. (see above import)
"""


def get_base_additional_count(grade):
    """
    Returns value of base --> based on index in an array.
    Returns additional count --> based on number of minuses and pluses.
    """

    grades = ["F", "FX", "E", "D", "C", "B", "A"]

    # Parse the input into a list
    if "+" in grade:
        arr = grade.split("+")
        additional_count = len(arr) - 1
    elif "-" in grade:
        arr = grade.split("-")
        additional_count = -(len(arr) - 1)
    else:
        arr = grade.split("-")
        additional_count = 0

    # Get base value
    base_value = grades.index(arr[0])

    return base_value, additional_count


def less_grade(A, B):
    """
    Compares two grades primarily based on their base,
    if bases are same, then it uses the additional count.
    """

    # Get grades
    gA, gB = A[1], B[1]

    # Parse the base and additional count of the grades
    gA_base, gA_add_count = get_base_additional_count(gA)
    gB_base, gB_add_count = get_base_additional_count(gB)

    # Compare the two values accordingly
    if gA_base == gB_base:
        return gA_add_count > gB_add_count
    else:
        return gA_base > gB_base


def main():

    # Read the input
    N = int(input())
    all_students = [input().split() for _ in range(N)]

    # Sort by name
    insertion_sort.sort(all_students)

    # Sort by grade
    insertion_sort._less = less_grade
    insertion_sort.sort(all_students)

    # Show the output
    for student in all_students:
        print(student[0])


if __name__ == "__main__":
    main()

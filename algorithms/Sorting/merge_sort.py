
# Merge sort - O(nlogn)
def merge_sort(input):

    size = len(input)

    # Base case
    if size < 2:
        return input

    # Spilt input array recursively
    else:
        mid = size // 2
        left = merge_sort(input[:mid])
        right = merge_sort(input[mid:])

    # Merging recursively
    return merge(input, left, right)


# Merge sub routine
def merge(input, left, right):

    i, j, k = 0, 0, 0

    # Comparing sub lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            input[k] = left[i]
            i += 1
            k += 1

        else:
            input[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        input[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        input[k] = right[j]
        j += 1
        k += 1

    return input

# Main function
def main():

    input = [5, 2, 1, 3, 6,
             4, 212, 100, 34
             ]
    merge_sort(input)
    print("Sorted List: ", input)

main()

# Quick sort main function
def quick_sort(input, start, end):

    # base case
    if start < end:
        pointer = partition(input, start, end)
        quick_sort(input, start, pointer-1)
        quick_sort(input, pointer+1, end)

    return None

# partition helper function
def partition(input, start, end):

    pivot = end
    pointer_index = start

    for i in range(start, end):
        if input[i] <= input[pivot]:
            input[pointer_index], input[i] = input[i], input[pointer_index]
            pointer_index += 1

    # Swapping pivot to the right position
    input[pointer_index], input[pivot] = input[pivot], input[pointer_index]

    return pointer_index


# Main function
def main():

    input = [5, 2, 1, 3, 6, 4, 212, 100, 34]
    quick_sort(input, 0, len(input)-1)

    print("Quick Sort: ", input)


# calling main
main()
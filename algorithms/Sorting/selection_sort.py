
# selection sort
def selection_sort(input):

    size = len(input)

    for i in range(size):

        # min element in each iteration
        min = i

        for j in range(i, size):
            if input[j] < input[min]:
                min = j

        input[min], input[i] = input[i], input[min]

    return input

# Main function
def main():

    input = [5, 2, 1, 3, 6, 4, 212, 100, 34]
    selection_sort(input)

    print("Selection Sort: ", input)


# calling main
main()
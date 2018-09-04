
# insertion sort - O(n^2)
def insertion_sort(input):

    size = len(input)

    for i in range(size):
        for j in range(i, 0, -1):
            if input[j] < input[j-1]:
                input[j], input[j-1] = input[j-1], input[j]

    return input

# Main function
def main():

    input = [5, 2, 1, 3, 6,
             4, 212, 100, 34
             ]
    insertion_sort(input)
    print("Insertion Sort: ", input)

# calling main
main()

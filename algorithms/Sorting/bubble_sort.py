
# Bubble Sort
def buble_sort(input):

    size = len(input)
    count = 1

    # Breaking the loop if given list is sorted
    while count != 0:
        for i in range(size-1, 0, -1):
            count = 0
            for j in range(0, i):
                if input[j] > input[j+1]:
                    input[j], input[j+1] = input[j+1], input[j]
                    count += 1

    return input


# Main function
def main():

    input = [5, 2, 1, 3, 6, 4, 212, 100, 34]
    buble_sort(input)

    print("Bubble Sort: ", input)


# calling main
main()
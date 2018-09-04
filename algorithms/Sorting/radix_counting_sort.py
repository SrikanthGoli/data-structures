
# Radix sort - O(nk)
def radix_sort(input):

    m = max(input)
    exp = 1

    while m/exp >= 1:
        counting_sort(input, exp)
        exp *= 10

    return None

# using counting sort as sub routine for sorting
def counting_sort(input, exp):

    size = len(input)
    count = [0] * 10
    output = [0] * size

    for i in range(size):
        index = input[i] / exp
        count[int(index % 10)] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(size-1, -1, -1):
        index = input[i] / exp
        output[count[int(index % 10)]-1] = input[i]
        count[int(index % 10)] -= 1

    for i in range(len(input)):
        input[i] = output[i]

    return None

def main():

    input = [5, 2, 1, 3, 6,
             4, 212, 100, 34
             ]
    radix_sort(input)
    print("Sorted List: ", input)

main()
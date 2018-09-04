
# Heap Sort Main Function - O(nlogn)
def heap_sort(input, type = None):

    size = len(input) - 1
    mid = size//2
    output = []

    while mid >= 0:
        if type == None or type == "Max":
            max_heapify(input, mid, size)
            mid -= 1
        else:
            min_heapify(input, mid, size)
            mid -= 1

    for i in range(size, -1, -1):
        output.append(input[0])
        input[0], input[i] = input[i], input[0]
        if type == None or type == "Max":
            max_heapify(input, 0, i-1)
        else:
            min_heapify(input, 0, i-1)

    return output

# Builds max heaps
def max_heapify(input, root, size):

    left_child = (root*2) + 1
    right_child = (root*2) + 2
    max = root

    if left_child <= size and input[left_child] >= input[max]:
        max = left_child

    if right_child <= size and input[right_child] >= input[max]:
        max = right_child

    if max != root:
        input[max], input[root] = input[root], input[max]
        root = max
        max_heapify(input, root, size)

    return None

# Build min heaps
def min_heapify(input, root, size):

    left_child = (root*2)+1
    right_child = (root*2)+2
    min = root

    if left_child <= size and input[left_child] <= input[min]:
        min = left_child
    if right_child <= size and input[right_child] <= input[min]:
        min = right_child

    if min != root:
        input[min], input[root] = input[root], input[min]
        root = min
        min_heapify(input, root, size)

    return None

def main():

    input = [5, 2, 1, 3, 6,
             4, 212, 100, 34
             ]
    print("Sorted List: ", heap_sort(input, "Min"))

# calling main
main()
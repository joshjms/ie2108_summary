# Making a heap from a list

def main():
    # Import the heap functions from Python's standard library
    from heapq import heappush, heappop

    # Initialize an empty list
    heap = []

    # Add elements to the heap
    heappush(heap, 1)
    heappush(heap, 3)
    heappush(heap, 2)

    # Remove elements from the heap
    print(heappop(heap)) # 1
    print(heappop(heap)) # 2
    print(heappop(heap)) # 3

# Using the heapq library, you don't have to perform siftup 
# and siftdown. The functions below are just for reference.

# Maxheap implementation in Python

def heapify(arr, n, i):
    # Initialize the largest element as the root
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If the left child is larger than the root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If the right child is larger than the root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change the root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root
        heapify(arr, n, largest)

def pop(arr):
    n = len(arr)
    arr[0], arr[n - 1] = arr[n - 1], arr[0]
    heapify(arr, n - 1, 0)
    return arr.pop()

def push(arr, item):
    arr.append(item)
    i = len(arr) - 1
    while i != 0 and arr[i] > arr[(i - 1) // 2]:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2

# P.S. these aren't bug tested. If there are any bugs, please let me know.
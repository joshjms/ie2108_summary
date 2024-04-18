# Merge Sort Algorithm
# Sorts the array by continuously dividing the array into two halves until the array is of length 1
# Then, merge the two halves by comparing the elements and sorting them
# Time complexity: O(N log N)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result
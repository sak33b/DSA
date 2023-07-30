# Assuming that the seq is sorted in descending order.
def binary_search(seq, query):
    left = 0
    right = len(seq) - 1
    while left <= right:
        mid = (left + right) // 2
        if seq[mid] == query:
            return mid
        elif seq[mid] < query:
            right = mid - 1
        elif seq[mid] > query:
            left = mid + 1

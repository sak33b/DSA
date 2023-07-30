# Assuming that the seq is sorted in descending order.
def binary_search(seq, query):
    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = (low + high) // 2
        if seq[mid] == query:
            return mid
        elif seq[mid] < query:
            high = mid - 1
        elif seq[mid] > query:
            low = mid + 1

    return None

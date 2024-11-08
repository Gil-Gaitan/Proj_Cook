def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements.
    target (int): The element to search for.

    Returns:
    int: The index of the target in the list, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

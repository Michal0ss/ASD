def search(nums, target):
    """
    Perform binary search on a sorted list to find the index of the target value.

    :param nums: List[int] - A sorted list of integers.
    :param target: int - The value to search for.
    :return: int - The index of the target in nums, or -1 if not found.
    """
    left, right = 0, len(nums) - 1

    while left<=right:
        mid = left + (right-left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

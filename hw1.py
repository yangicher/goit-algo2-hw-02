def find_min_max(arr):
    if not arr:
        raise ValueError("Empty array is not allowed")

    def helper(left, right):
        if left == right:
            return arr[left], arr[left]

        if right == left + 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]

        mid = (left + right) // 2
        min_left, max_left = helper(left, mid)
        min_right, max_right = helper(mid + 1, right)

        return min(min_left, min_right), max(max_left, max_right)

    return helper(0, len(arr) - 1)


if __name__ == "__main__":
    arr = [3, 5, 1, 8, 2, -4, 7, 6, 0, 9]
    min_val, max_val = find_min_max(arr)

    print("Min: ", min_val)
    print("Max: ", max_val)
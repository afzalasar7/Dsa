#Template to solve Sliding Window Problem
# Ex Problem: Find the length of the longest subarray with sum <= k

arr = [2, 5, 1, 7, 10]
k = 14

# 1. Brute Force Approach (O(N^2))
def longest_subarray_brute_force(arr, k):
    n = len(arr)
    max_len = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum <= k:
                max_len = max(max_len, j - i + 1)
            else:
                break  # Optimization: Stop checking further as sum exceeded k

    return max_len

print(longest_subarray_brute_force(arr, k))


# 2. Optimized Sliding Window Approach (O(2N) ≈ O(N))
def longest_subarray_sliding_window(arr, k):
    
    n = len(arr)
    max_len = 0
    left = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += arr[right]

        # Shrink the window when sum exceeds k
        while curr_sum > k and left <= right:
            curr_sum -= arr[left]
            left += 1

        # Update max_len after adjusting the window
        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_subarray_sliding_window(arr, k))


# 3. Optimal Approach (O(N)) - Specialized Version
def longest_subarray_optimized(arr, k):
    """
    Optimized approach to find the longest subarray with sum <= k.
    
    Note: This version is optimized for finding the maximum length but won't work
          if we need to return the exact subarray.
    """
    n = len(arr)
    max_len = 0
    left = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += arr[right]

        # Move the left pointer only when necessary
        if curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_subarray_optimized(arr, k))

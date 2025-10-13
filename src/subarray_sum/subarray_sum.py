def subarray_sum(arr, target):
    prefix_sums = {0: -1}  # sum: index
    cur_sum = 0
    for i, num in enumerate(arr):
        cur_sum += num
        complement = cur_sum - target
        if complement in prefix_sums:
            return (prefix_sums[complement] + 1, i + 1)
        prefix_sums[cur_sum] = i
    return None


subarray_sum([1,3,-3,8,5,7],5)
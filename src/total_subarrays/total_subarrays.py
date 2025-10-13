def subarray_sum_total(arr: list[int], target: int) -> int:
    prefix_sums = {0: 1}
    curr_sum = 0
    counter = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        # print("arr[i]: ", arr[i])
        # print("curr_sum: ", curr_sum)
        complement = curr_sum - target
        # print("complement: ", complement, "=", curr_sum, "-", target)
        if complement in prefix_sums:
            counter += prefix_sums[complement]
            # print(counter)
        if curr_sum in prefix_sums:
            prefix_sums[curr_sum] += 1
        else:
            prefix_sums[curr_sum] = 1
        # print("prefix_sum: ", prefix_sums, "\n")
    return counter
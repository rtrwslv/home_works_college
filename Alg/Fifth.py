def findKthLargest(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]

print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
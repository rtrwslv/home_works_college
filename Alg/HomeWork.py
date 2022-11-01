from operator import indexOf


def twoSum(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums and target - nums[i] != nums[i]:
            return[i, indexOf(nums, target - nums[i])]
        
print(twoSum(nums = [2,7,11,15], target = 9))
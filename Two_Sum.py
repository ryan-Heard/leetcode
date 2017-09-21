class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            potential_value = target - i

            print(nums[nums.index(i)+1::])
            if potential_value == i and i in nums[nums.index(i)+1::]:
                return [
                            nums.index(i),
                            nums[nums.index(i)+1::].index(i) +
                            nums.index(i) + 1
                        ]

            if potential_value in nums and potential_value != i:
                return [nums.index(i), nums.index(potential_value)]


if __name__ == '__main__':
    nums, target = [3, 3], 6
    print(Solution().twoSum(nums, target))

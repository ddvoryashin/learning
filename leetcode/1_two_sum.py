#class Solution:
#    def twoSum(self, nums: list[int], target: int) -> list[int]:
#        for i, v1 in enumerate(nums):
#            for j, v2 in enumerate(nums[i + 1:]):
#                if v1 + v2 == target:
#                    l = []
#                    l.append(i)
#                    l.append(j + i + 1)
#                    print(l)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in hashmap.keys():
                return [i, hashmap.get(value)]
            else:
                hashmap[value] = i


sol = Solution()
nums = [1, 3, 5, 7]
tgt = 8
print(sol.twoSum(nums, tgt))

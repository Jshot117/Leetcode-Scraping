# Majority Element
**Language:** python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #example arr= [1,1,7,1,8,1,1] majority element is 1
        #example arr = [3,4,5,4,4,4,2] --4

        nums_counter = Counter(nums)
        print(nums_counter.most_common())
        return nums_counter.most_common()[0][0]
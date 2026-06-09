class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ""
        for i in digits:
            nums += str(i)

        nums = int(nums) + 1
        arr = []
        for j in str(nums):
            arr.append(int(j))

        return arr

        

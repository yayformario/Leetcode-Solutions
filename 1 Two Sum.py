from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Quick exit
        if len(nums) == 2:
            return([0,1])
        
        #Initialize return array and hashmap {diff:index}
        ans = []
        hash = {}

        #Loop entire array
        for right in range(len(nums)):
            #Check if our value is already in hash
            if nums[right] in hash:
                ans.append(right)
                ans.append(hash.pop(nums[right]))
                return ans
            
            #Add difference to hash as it might be one of the pairs
            #{value:index}
            diff = target - nums[right]
            hash[diff] = right

        #Default exit
        return (ans)
    

#Create solution object
testing = Solution()


inputs = [
    #Given input
    [[2,7,11,15],9], #[0,1]
    [[3,2,4],6],#[1,2]
    [[3,3],6],#[0,1]
]

#Loop all input
for input in inputs:
    print(str(testing.twoSum(input[0], input[1])))

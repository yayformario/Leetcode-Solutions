from typing import List

class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        #not sorted; hash

        duplicates = set()

        for num in nums:
            #return True when we find duplicates
            if num in duplicates:
                return True

            duplicates.add(num)
        
        #If at EOL; no duplicates found
        return False
    
testing = Solution()

input = [
    #given input
    [1,2,3,1], #True
    [1,2,3,4], #False
    [1,1,1,3,3,4,3,2,4,2] #True
]

for ex in input:
    print(str(testing.containsDuplicate(ex)))
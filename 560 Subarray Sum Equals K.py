from typing import List

class Solution:
    #Given an array of integers and integer k
    #Returning total number of subarrays whose sum equals to k
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        #Can track a prefixSum and 'chop' off blocks to get to k
        #Need an offset to chop off from our prefixSum
        #We have: currSum and k
        #currSum = k + offset; offset can be zero ofc
        #offset = currSum - k 
        prefixSum = {0:1}
        currSum = 0
        for num in nums:
            #Calculate current sum and offset
            currSum += num 
            offset = currSum - k

            #Check if we've seen this offset in our prefixSum
            if offset in prefixSum:
                #If so, we can 'chop' it off and get k
                #Thus it's a solution
                ans += prefixSum.get(offset)
            
            #Add the currSum to our prefixSum
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
            
        return ans
    
testing = Solution() 

examples = [

    #Missed test cases
    [[1,-1,0],0], #3

    #Misc examples
    [[-2,3,-10,15,-3,7,-1,10,-2], 8], #3
    [[44,3,1,-12,16],8],#1
    #Given examples
    [[1,1,1],2], #2
    [[1,2,3],3], #2
]

for ex in examples:
    print(str(testing.subarraySum(ex[0],ex[1])))



        
from typing import List

class Solution:
    def removeDuplicates (self, nums: List[int]) -> int:
        returnVal = 0
        duplicateTolerance = 2
        leftPointer = 0
        currentCount = 0
        #We want to loop the entire array
        for rightPointer in range(len(nums)):
            #Check to see if rightPointer is not a duplicate
            if nums[leftPointer] == nums[rightPointer]:
                currentCount += 1

                #Check to see if we're beyond our tolerance for duplicates
                if currentCount <= duplicateTolerance :
                    returnVal += 1

            #We encountered a new value value
            #We only want to move leftPointer when we encounter new values 
            else:
                #Edge case where we encountered more than 2 or duplicates: [0,0]
                #We want to move pointer over by two elements
                if (currentCount >= duplicateTolerance):
                    leftPointer += 2
                    nums[leftPointer] = nums[rightPointer]
                
                #Otherwise, we only encountered the value once
                else: 
                
                #Update the vale at leftPointer
                nums[leftPointer] = nums[rightPointer]

                #Update counters
                currentCount = 1
                returnVal += 1

        return returnVal
        

    

testing = Solution()

examples = [
    [1,1,1,2,2,3], #5: [1,1,2,2,3]
    [0,0,1,1,1,1,2,3,3], #7: [0,0,1,1,2,3,3]

    #Single element edge cases:
    [0], #Return 1: 0
    [-1], #[-1]
    [100,], #100

    #Two element edge cases:
    [0,0], #2: [0,0]
    [1,1], #2: [1,1]

    #Three elemet edge cases:
    [1,2,3], #3: [1,2,3]
    [1,1,2], #3
    [3,3,3], #2: [3,3]

    #All same elements: returnVal < len(nums)
    [0,0,0,0,0], #2: [0,0]
    
    #All unique elements: returnVal == len(nums)
    [1,2,3,4,5,6], #6: [1,2,3,4,5,6]

    #Cases where elements appear twice: returnVal == len(nums)
    [1,1,2,2,3,3,4,4], #8: [1,1,2,2,3,3,4,4]

    #Cases where elements appear three times: returnVal < len(nums)
    [0,0,0,1,1,1,2,2,2]: #6: [0,0,1,1,2,2]

    #Mixed cases of elements appaearing once and twice returnVal == len(nums)
    [0,1,2,2,3,4,5,5]#8: [0,1,2,2,3,4,5,5]

    #Mixed cases of elements appearing once and three times: returnVal < len(nums)
    [0,0,0,1,2,3,3,3,4,5,5,5]# 9: [0,0,1,2,3,3,4,5,5]

    #Mixed cases of elements appearing twice and three times: returnVal < len(nums)
    [1,1,2,2,2,3,3,4,4,4,5,5] # 10 : [1,1,2,2,3,3,4,4,5,5]

    #Mixed cases with elmeents appearing once, twice, three times: returnVal < len(nums)
    [0,0,0,1,2,3,3,4,4,4,5,6,6,7,8,8,8,9,10] # 16: [0,0,1,2,3,3,4,4,5,6,6,7,8,8,9,10]
]

for ex in examples:
    print("Input: " + str(ex))
    ans = testing.removeDuplicates(ex)
    print("Return Value: " + str(ans))
    ans += 1
    print("Output: " + str(ex[:ans]) + "\n")
    

"""
Notes:
- Remove duplicates, only allowing elements appearing twice
- has to be in place; O(1) memory
- Keep relative order of the elements
- The first k elements should hold the final result

Constraints:
- Gauranteed at least 1 element
- Negative values
- Already sorted
"""
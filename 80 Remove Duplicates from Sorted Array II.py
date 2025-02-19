from typing import List

class Solution:

    def removeDuplicatesHash(self, nums: List[int]) -> int:
        #Quick exits:
        if (len(nums) <= 2):
            return len(nums)
        
        #left pointer with offset will be our return value
        leftPointer = 0
        appearanceCounter = 0

        #right pointer will loop the entire array
        for rightPointer in range(len(nums)):
            #Check to see if we encountered a duplicate
            if (nums[leftPointer] == nums[rightPointer]):
                #increment the counter; don't move pointer just yet
                appearanceCounter += 1
            #We only move leftPointer when:
            #1. We encounter a new value
            #2. We only have 1 duplicate
            #Note: Always update the array to avoid edge cases
            else:
                #Different value; move pointer, update value, reset duplicates counter
                leftPointer += 1
                nums[leftPointer] = nums[rightPointer]
                appearanceCounter = 1

            #Move left pointer if it's our first duplicate
            if (appearanceCounter == 2):
                leftPointer += 1
                nums[leftPointer] = nums[rightPointer]


        return (leftPointer + 1)
    
    def removeDuplicates (self, nums: List[int]) -> int:
        #Early exit:
        if (len(nums) <= 2):
            return len(nums)
        
        
        #At this point, we're gauranteed 3 or more elements
        #We are checking for duplicates
        leftPointer = 0
        rightPointer = 1
        hasDuplicate = 0 #0: false | 1: true

        
        #Right pointer always loops until end of list
        while rightPointer < len(nums):
            if (nums[leftPointer] == nums[rightPointer]):
                #Check to see if this number has not previously had a duplicate
                if hasDuplicate == 0:
                    #crawl left pointer and update the duplicate
                    leftPointer += 1
                    nums[leftPointer] = nums[rightPointer]
                    hasDuplicate = 1

            else:
                #We encounter a brand new value
                #Incremenet leftPointer
                leftPointer += 1
                #Update value
                nums[leftPointer] = nums[rightPointer]
                #reset hasduplicate
                hasDuplicate = 0
            
            rightPointer += 1
        
        #Left pointer with offest is our anaswer
        return (leftPointer + 1)
        

    

testing = Solution()

examples = [
    

    

    #Three elemet edge cases:
    [1,2,3], #3: [1,2,3]
    [1,1,2], #3: [1,1,2]
    [3,3,3], #2: [3,3]

    #All same elements: returnVal < len(nums); left pointer never moves case
    [0,0,0,0,0], #2: [0,0]
    
    #All unique elements: returnVal == len(nums), nothing gets updated
    [1,2,3,4,5,6], #6: [1,2,3,4,5,6]

    #Cases where elements appear twice: returnVal == len(nums), nothing gets updated
    [1,1,2,2,3,3,4,4], #8: [1,1,2,2,3,3,4,4]

    #Cases where elements appear three times: returnVal < len(nums)
    [0,0,0,1,1,1,2,2,2], #6: [0,0,1,1,2,2]

    #Mixed cases of elements appaearing once and twice returnVal == len(nums)
    [0,1,2,2,3,4,5,5],#8: [0,1,2,2,3,4,5,5]

    #Mixed cases of elements appearing once and three times: returnVal < len(nums)
    [0,0,0,1,2,3,3,3,4,5,5,5],# 9: [0,0,1,2,3,3,4,5,5]

    #Mixed cases of elements appearing twice and three times: returnVal < len(nums)
    [1,1,2,2,2,3,3,4,4,4,5,5], # 10 : [1,1,2,2,3,3,4,4,5,5]

    #Mixed cases with elmeents appearing once, twice, three times: returnVal < len(nums)
    [0,0,0,1,2,3,3,4,4,4,5,6,6,7,8,8,8,9,10], # 16: [0,0,1,2,3,3,4,4,5,6,6,7,8,8,9,10]

    #Given examples
    [1,1,1,2,2,3], #5: [1,1,2,2,3]
    [0,0,1,1,1,1,2,3,3], #7: [0,0,1,1,2,3,3]

    #Single element edge cases:
    [0], #Return 1: 0
    [-1], #[-1]
    [100,], #100

    #Two element edge cases:
    [0,0], #2: [0,0]
    [1,1], #2: [1,1]
]

for ex in examples:
    print("Input: " + str(ex))
    ans = testing.removeDuplicates(ex)
    print("Return Value: " + str(ans))
    print("Output: " + str(ex[:ans]) + "\n")
    

"""
Notes:
It might seem like "useless" work to update everytime leftPointer moves but it causes too many edge cases
ALWAYS update element at leftPointer if it moves to make the problem significantly easier
Description:
- Remove duplicates, only allowing elements appearing twice
- has to be in place; O(1) memory
- Keep relative order of the elements
- The first k elements should hold the final result

Constraints:
- Gauranteed at least 1 element
- Negative values
- Already sorted

#Notes:
Cases with all unique elements never gets shifted:
[1,2,3,4,5,6,7]

Our (return value == len(nums)) if we never encounter a variable more than twice
[1]
[0,0]
[1,1,2,2,3,3]
[4,5,6,6,7]

#We don't always have to shift 3+ element appearances
[3,3,3] -> [3,3]
#[1,2,3,4,5,5,5,5,5,5] - > [1,2,3,4,5,5]

#But 3+ element appearances are the only times we have to consider shifting
[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

"""
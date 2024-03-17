from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        #Two pointer approach
        leftPointer = 0
        rightPointer = len(height) - 1

        maxLeft = 0
        maxRight = 0

        trappedWater = 0

        #Loop until pointers cross
        
        while leftPointer < rightPointer:
            #Crawl the smaller pointer; default to crawling right pointer if equal heights (no real reason)
            if height[leftPointer] < height[rightPointer]:
                
                #trapped water = (maxLeft) - (height[leftPointer])
                #So sum += (maxLeft) - (height[leftPointer])
                #To avoid adding negatives; add kadane's algo
                #sum += max((maxLeft) - (height[leftPointer]), 0)
                trappedWater += max(maxLeft - height[leftPointer], 0)

                #update maxLeft and shift the pointer as needed
                maxLeft = max(maxLeft, height[leftPointer])
                leftPointer += 1

            else:
                trappedWater += max(maxRight - height[rightPointer], 0)

                maxRight = max(maxRight, height[rightPointer])
                rightPointer -= 1


        return trappedWater

testing = Solution()

examples = [
    #Given examples:
    [0,1,0,2,1,0,1,3,2,1,2,1], #6
    [4,2,0,3,2,5], #9
]

for ex in examples:
    print(
        "Height = " + str(ex) + "\n" +
        "Output " + str(testing.trap(ex)) + "\n"
    )

"""
Notes: 
We know that the smaller of the heights determines how much water can "roll over" 

Constraints:
- We are gauranteed at least 1 element
- The heights of the elements can be zero (No negatives)
"""
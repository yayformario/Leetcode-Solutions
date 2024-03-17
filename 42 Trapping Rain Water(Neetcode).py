from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        
        #We are going to need to pointers
        rightPointer = len(height) - 1

        #Keep track of the highest left pointer and keep a log
        leftMax = 0
        leftMaxHeights = [0] * len(height)


        #Keep track of the highest right pointer and keep a log 
        rightMax = 0
        rightMaxHeights = [0] * len(height)

        #At any given point, the max water we can trap is based on the lower bar
        minHeights = [0] * len(height)

        #O(n)
        for leftPointer in range(len(height)):
            #Store the highest max that's on the LEFT SIDE of our current spot
            leftMaxHeights[leftPointer] = leftMax
            #Update current left max for the next iteration
            leftMax = max (leftMax, height[leftPointer])
            
            #Store the highest max that's on the RIGHT SIDE of our current spot
            rightMaxHeights[rightPointer] = rightMax
            #Update current right max for the next iteration
            rightMax = max(rightMax, height[rightPointer])
            rightPointer -= 1

        #We can now loop to find all current heights for Sum
        """
        The amount of water we can hold is based on:
            min(leftMaxHeights[i], rightMaxHeights[i]) - heights[i]
        
        To avoid negatives, we can combine Kadan'es algo:
        max(min(...), 0)
        """
        for i in range(len(minHeights)):
            sum += max(min(leftMaxHeights[i], rightMaxHeights[i]) - height[i], 0)

        
        return sum

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


Constraints:
- We are gauranteed at least 1 element
- The heights of the elements can be zero (No negatives)
"""

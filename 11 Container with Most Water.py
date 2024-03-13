from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        #Two pointer approach
        leftPointer = 0
        rightPointer = len(height) - 1

        #We have two Goals: Find the max height, find the max area
        maxHeight = [0,0] #Stores [height, pointer]
        maxArea = 0

        #Loop until pointers cross
        while leftPointer < rightPointer:
            """
            Gameplan:
            1. Find the taller of the two for our start/endpoint
            2. Use the smaller of the two to find currentArea
            3. Update maxArea and currentHeight as needed
            4. Crawl the pointer that had the smaller height value
            """

            #Find the Taller of the two for our start/endpoint; store currentHeight
            if (height[leftPointer] > height[rightPointer]):
                
                #Store maxheight as needed
                if (height[leftPointer] > maxHeight[0]):
                    maxHeight[0] = max(maxHeight[0], height[leftPointer])
                    maxHeight[1] = leftPointer

                #Use the other pointer to calculate the area
                areaLength = rightPointer - leftPointer
                areaHeight = height[rightPointer]
                maxArea = max(maxArea, (areaLength * areaHeight))

                #Crawl the smaller pointer
                rightPointer -= 1

            #Same thing but for right pointer
            else:
                
                if (height[rightPointer] > maxHeight[0]):
                    maxHeight[0] = max(maxHeight[0], height[rightPointer])
                    maxHeight[1] = rightPointer

                #Use the other pointer to calculate the area
                areaLength = rightPointer - leftPointer
                areaHeight = height[leftPointer]
                maxArea = max(maxArea, (areaLength * areaHeight))

                #Crawl the smaller pointer
                leftPointer += 1

            
        return maxArea

    
testing = Solution()

examples = [
    #Given examples:
    [1,8,6,2,5,4,8,3,7], #49
    [1,1] #1
]

for ex in examples:
    print(
        "Height: " + str(ex) + "\n"
        "Output: " + str(testing.maxArea(ex)) + "\n"
        )
    
"""
Notes:
Ignoring the description and focusing soley on the image provided + solution:
- We just wan to return the largest area  between to bars 
    - (length x height) 

The two highest bars are not always the correct answer: 
- A singular highest bar will ALWAYS be included in the length
    -It will either be the starting point or ending point of the length

- We can get the length by (right pointer - leftPointer)
    - From example one: 
        - leftPointer = 1
        - rightPointer = 8
        - (rightPointer - leftPointer) = 7

- The second bar will determine our answer; the height used for finding area
    - From example one: (7)


Constraints:
- Guaranteed at least two bars
- No "negative heights" but the height of something can be zero
"""
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #Initilize return array
        ans = []
        #Need to maintain pointers for sliding window
        left = 0
        #Deque to track maximum value
        dq = deque()

        #Loop entire array
        for right in range(len(nums)):
            #Reused vars for readability
            value = nums[right]

            #Add value only when: (dq is empty) or (value is larger than recent dq entries)
            #Translate: Pop only when: (dq exist) and (recent dq entry is smaller than value)
            while dq and dq[-1] < value:
                dq.pop()
            
            #Ready to add our value to dq
            dq.append(value)

            #Check if we need to move our window
            if (right - left + 1) > k:
                #Might be largest value; if so remove it
                if dq[0] == nums[left]:
                    dq.popleft()
                left += 1
            
            #Add the current largest to our return array
            #ONCE we hit window size
            if (right - left +1 == k):
                ans.append(dq[0])
        return(ans)


 
testing = Solution()

testCases = [
    #Given test cases
    [[1,3,-1,-3,5,3,6,7],3],
    [[1], 1],

    #All negative values
    [[-1,-2,-100,-5,-16,-20,-1,-100], 5],

    #Same size window
    [[1,2,-5],3],

    #small window
    [[5,1,1,1,5],2],

]

for case in testCases:
    print('MaxSum is: ' + str(testing.maxSlidingWindow(case[0], case[1])))
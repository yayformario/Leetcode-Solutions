from typing import List

    #Brute force: O(n * n * n)
    #Merge: O(n log n) 
    #Once merged, can single pass for multiple answers
    #Is O(3n) possible? 
    #- Without sorting, can accidentally 'skip' potential solutions

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)

        #prep pointers
        base = 0

        #Sort to check for early exits
        nums.sort()
        if nums[0] > 0 or nums[length-1] < 0:
            return ans
        
        #Loop base; ensure other points aren't OOB
        while base < length-2:

            #The rest is 2SUM
            left = base + 1
            right = length-1
            
            #Searching for target to ensure we're only looking for pairs
            # 0 = base + left + right -> -base = left + right -> target = -base
            target = -nums[base]
            while left < right:
                #There might a potential solution for early exits here; but haven't coded it
                sum = nums[left] + nums[right]
                #Skip any duplicates right off the bat
                #offset by 1 to cover the edge case of last 3 variables
                if sum > target:
                    temp2 = nums[right]
                    while temp2 == nums[right] and left<right:
                        right -=1
                elif sum < target:
                    temp2 = nums[left]
                    while temp2 == nums[left] and left < right:
                        left +=1
                else:
                    ans.append([nums[base], nums[left], nums[right]])
                    #Since we no longer need the solution, skip all duplicates
                    temp2 = nums[left]
                    while temp2 == nums[left] and left < right:
                        left +=1

            #Check if we need to increment or skip duplicates after first pass through
            temp = nums[base]
            while temp == nums[base] and base < length-2:
                base+=1
        return ans



testing = Solution()

examples = [

    #All positives/negatives
    [-12,-9,-4,-100,-55], #[]
    [12,5,67,43,50,100,101], #[]

    #all zeros
    [0,0,0,0,0,0,0,0,0,0,0,0], #[0,0,0]

    #Answer at the start or end
    [-2,0,2,15,15,15,15,15],#[-2,0,2]
    [-1,0,1,5,5,5,5,5,5,5,5,5,5,5], #[1,0,-1]

    [-15,-15,-15,-15,-2,0,2],#[-2,0,2]
    [5,5,5,5,5,5,5,5,5,5,5,1,0,-1], #[1,0,-1]

    [-100,-50,0,50,100],#[-100,0,100] [-50,0,50]
    [-1,0,1,5,5,5,5,5,5,5,5,5,5,5,1,0,-1], #[1,0,-1]

    #No solution
    [-3,-2,-1,12,13,14,15], #[]
    [-4,-3,-2,-1,15,14,13,12], #[]
    [-2,-2,-2,-2,15,15,15,15], #[]

    #Solution at edges
    [100,0,-100,-2,15,15,15,15],#[-100,0,100]


    #Given examples
    [-1,0,1,2,-1,-4], #[-1,-1,2], [-1,0,1]
    [0,1,1], #[]
    [0,0,0], #[0,0,0]

    ]

for ex in examples:
    print(str(testing.threeSum(ex)))


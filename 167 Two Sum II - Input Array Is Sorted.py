from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Quick exit since we're guaranteed an answer
        if len(numbers) == 2:
            return [1,2]
        
        #Initialize return array
        ans = []

        #Solution must be O(1) space time; two pointers
        leftPointer = 0
        rightPointer = len(numbers) - 1

        #Loop until we find solution or pointers cross
        #Lowkey, pointers should never cross but it's an emergency exit
        
        while leftPointer < rightPointer:
            #variables for readability
            sum = numbers[leftPointer] + numbers[rightPointer]
            #Everything is sorted, just look for target
            if sum == target:
                ans.append(leftPointer+1)
                ans.append(rightPointer+1)
                return ans
            
            elif sum > target:
                #Loop through any duplicates
                currentVal = numbers[rightPointer]
                while currentVal == numbers[rightPointer]:
                    rightPointer -= 1
            else:
                #Loop through any duplicates
                currentVal = numbers[leftPointer]
                while currentVal == numbers[leftPointer]:
                    leftPointer += 1

        return ans
    
testing = Solution()

examples = [
    #Given inputs
    [[2,7,11,15],9], #[1,2]
    [[2,3,4], 6], #[1,3]
    [[-1,0],-1], #[1,2]

    #Duplicates
    [[1,1,1,1,3,3,7,7,7,7,7,7,7], 6], #[5,6]
]

for ex in examples:
    print(str(testing.twoSum(ex[0],ex[1])))
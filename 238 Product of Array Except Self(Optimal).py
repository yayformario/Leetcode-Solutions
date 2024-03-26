from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productExceptSelf = [1] * (len(nums))

        #Calculate the prefixProduct
        #Calculate the suffixProduct
        prefixProduct = 1
        suffixProduct = 1 
        
        for leftPointer in range(len(nums)):
            
            #Handle the left side first
            # Add the current value first before modifying it
            # #calculate product for next iteration
            productExceptSelf[leftPointer] = prefixProduct
            prefixProduct *= nums[leftPointer]

        for rightPointer in range(len(nums) -1 , -1, -1):
            #Handle right side the same way
            # Multiple our suffix to the list of prefix
            # Calculate product for next iteration
            productExceptSelf[rightPointer] *= suffixProduct
            suffixProduct *= nums[rightPointer]
        
        return productExceptSelf
        
testing = Solution()

examples = [
    #Given examples:
    [1,2,3,4], #[24,12,8,6]
    [-1,1,0,-3,3], #[-1,1,0,-3,3]

]

for ex in examples:
    print(
        "Input " + str(ex) + "\n" + 
        "Output" + str(testing.productExceptSelf(ex))
    )
"""
Restrictions:
- O(n) solution
- Can't use division operation 
- at least a length of 2 elements
- negative values
- product is gauranteed to fit in a 32-bit integer

"""
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
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        #Get a prefixProduct and suffixProduct
        #Our answer should be: (prefixProduct left of i) + (suffixProduct right of i)
        #set to 1 for now since we're dealing with products
        #This is to avoid accidentally setting everything to zero right off the bat
        leftProduct = 1
        rightProduct = 1
        
        prefixProduct = [0] * len(nums)
        suffixProduct = [0] * len(nums)

        #Initialize rightPointer to reduce number of loops by 1
        rightPointer = len(nums) - 1

        #return value
        ans = [0] * len(nums)
        #Loops nums once, but calculate both at the same time
        #O(n)
        for leftPointer in range(len(nums)):
            #Calculate prefixProduct
            leftProduct *= nums[leftPointer]
            prefixProduct[leftPointer] = leftProduct

            #Calculate suffixProduct and decrement the pointer
            rightProduct *= nums[rightPointer]
            suffixProduct[rightPointer] = rightProduct
            rightPointer -= 1

        #O(n) 
        for i in range(len(nums)):
            #Two edge cases; first and last elements
            if i == 0:
                ans[i] = suffixProduct[i+1]
            elif i == (len(nums) - 1):
                ans[i] = prefixProduct[i-1]
            else:
                ans[i] = prefixProduct[i-1] * suffixProduct[i+1]      

        return ans
        
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
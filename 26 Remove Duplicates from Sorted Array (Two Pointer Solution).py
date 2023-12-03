class Solution(object):
    def removeDuplicates (self, nums):

        """
      26 Remove Duplicates from Sorted Array (Two Pointer Solution)  Two Pointer Approach:
        Runtime: O(n) | O(n + 1) 
        Spacetime: O(1) | Only a constant value L was generated 
        """
        
        #Index L that crawls array | O(1) spacetime
        L = 0

        #R is going to loop entire array | O(n) runtime
        for R in nums:
            '''
            We only want to return a list of unique values
                L index will store all the unique values
                L will only crawl forward after a unique value is found
                L is only updated when a unique value is found
                    nums[L] != R
            '''
            
            #Unique value is found | O(1) runtime: updating pointer and array value is constant time
            if (nums[L] != R):
                #increment Pointer for a new unique value
                L += 1

                #Update the array
                nums[L] = R

        #Since L index started at 0, the number of unique values is (L + 1)
        return (L + 1)


testing = Solution()
example = [1,1,2]
example2 = [0,0,1,1,1,2,2,3,3,4]
example3 = [0,0,0,0,0]
example4 = [1,2,3,4,5]

print(testing.removeDuplicates(example))
print(testing.removeDuplicates(example2))
print(testing.removeDuplicates(example3))
print(testing.removeDuplicates(example4))

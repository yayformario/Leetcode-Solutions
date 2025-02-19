class Solution(object):
    def twoPointerSolution (self, nums):

        """
        26 Remove Duplicates from Sorted Array (Two Pointer Solution)  Two Pointer Approach:
        Runtime: O(n) | O(n + 1) 
        Spacetime: O(1) | Only a constant value L was generated 
        """
        
        #Index L that crawls array | O(1) spacetime
        L = 0

        #R is going to loop entire array | O(n) runtime
        for R in nums:
            """
            We only want to return a list of unique values
                - L index will store all the unique values
                - L will only crawl forward after a unique value is found
                - L is only updated when a unique value is found
                    - nums[L] != R

            Return the number of unique elements:
            - We're gauranteed at least 1 element
                - The minimum return value is 1
            
            Since L starts at 0 and only increments for every extra unique value
                - We return (L + 1)
            """
            
            #Unique value is found | O(1) runtime: updating pointer and array value is constant time
            if (nums[L] != R):
                #increment Pointer for a new unique value
                L += 1

                #Update the array
                nums[L] = R

        #(L + 1) due to L starting at 0 and we're gauranteed at least 1 element to return
        return (L + 1)

    def hashSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Hashing Approach
        Runtime: O(n) | O(n + 1)
        Spacetime: O(n) | No duplicates & hashset == len(nums)
            ==--- Does not qualify as a solution!---== 
        """

        '''
        Remove duplicates in place
            relative order should be kept the same; return only unique elements

        First k elements of nums contain the unique elements
            remaining elements of nums are not important as well as size of nums
        
        Return k

        Output: k, array 
        '''
        #Create return value k and set to zero for default
        k = 0
        
        #Create a hash set to check for duplicates
        duplicates = set()

        #We want to loop the entire array | O(n) runtune
        for n in nums:
            #Check to see if current number is in hash set | (O(k), k == # of unique elements)
            if not (n in duplicates):
                #Add item to our hash set | O(1) constant time
                duplicates.add(n)

                #Update the value in the return array | O(1) constant time
                nums[k] = n

                #increment for next value | O(1) constant time
                k += 1
            
        return k


testing = Solution()
example = [1,1,2]
example2 = [0,0,1,1,1,2,2,3,3,4]
example3 = [0,0,0,0,0]
example4 = [1,2,3,4,5]

print(testing.hashSolution(example))
print(testing.hashSolution(example2))
print(testing.hashSolution(example3))
print(testing.hashSolution(example4))

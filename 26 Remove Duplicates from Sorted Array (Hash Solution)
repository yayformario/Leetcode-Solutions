class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Hashing Approach

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

        #We want to loop the entire array
        for n in nums:
            #Check to see if current number is in hash set
            if not (n in duplicates):
                #Add item to our hash set
                duplicates.add(n)

                #Update the value in the return array
                nums[k] = n

                #increment for next value
                k += 1
            
        return k


testing = Solution()
example = [1,1,2]
example2 = [0,0,1,1,1,2,2,3,3,4]

print(testing.removeDuplicates(example))
print(testing.removeDuplicates(example2))


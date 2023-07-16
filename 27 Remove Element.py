class Solution (object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        """
        Given:
            nums - integer array
            val - integer
            k - number of elements in nums not equal to val 
            return - k

        Change the array nums such that the first k elements of nums contains values not equal to val
            The remaining elements are not important
        """

        '''
        Two pointer approach
        Runtime: O(n) | O(n + 1)
        SpaceTime: O(1) |L index
        '''
        #L index | O(1) spacetime
        L = 0
        #R will loop entire array | O(n) runtime
        for R in nums:
            '''
            R will slowly add values to nums[L] that are not R
                O(1) runtime | constant time for changing values and incrementing 
            '''
            if R != val:
                #update array and increment
                nums[L] = R
                L += 1
        
        '''
        k = # of elements in nums not equal to val
        k = L (size of elements without val) 
        '''

        return L

testing = Solution()

example1 = [3,2,2,3]
val1 = 3

example2 = [0,1,2,2,3,0,4,2]
val2 = 2

print(testing.removeElement(example1, val1))
print(testing.removeElement(example2, val2))




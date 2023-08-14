class Solution (object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        We want to create array: ans
        of length: 2n
        where: ans[i] == nums[i]
        and: ans[i+n] == nums[i]
        for: 0 <= i < n
        Specifically: Ans is the concatenation of two nums arrays
        """

        """
        1 Pointer solution
        Runtime: O(n) | O(2n + 2n) -> O(4n) 
        Spacetime: O(n) | O(2n + 1) 
        """

        #We will be using len(nums) multiple times
        #Spacetime: O(1)
        length = len(nums)
        
        #Create an array that's 2n
        #Runtime: O(2n)
        #Spacetime: O(2n)
        ans = [0] * (2*length)

        """
        Total runtime: O(2n)
        """
        #Loop every value
        #Runtime: O(n) 
        for R in range(len(nums)):
            #Assign the value to i and (i+length)
            #Runtime: O(2) 
             ans[R] = nums[R]
             ans[R+length] = nums[R]
        return ans

testing = Solution()
example1 = [1,2,1]
example2 = [1,3,2,1]

print(testing.getConcatenation(example1))
print(testing.getConcatenation(example2))
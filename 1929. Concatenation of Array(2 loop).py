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
        2 Loops solution
        Runtime: O(n) | O(2n)
        Spacetime: O(n) | O(2n)
        """

        #Array that will eventually grow to 2n
        #Spacetime: O(2n)
        ans = []

        """
        Total runtime: O(2n)
        Total spacetime: O(2n)
        """
        #Loop every value twice
        #Runtime: O(2) 
        for i in range(2):
            #Runtime: O(n)
            for n in nums:
                #Assign the value to i and (i+length)
                #Runtime: O(1) 
                #Spacetime: O(1)
                ans.append(n)
        return ans

testing = Solution()
example1 = [1,2,1]
example2 = [1,3,2,1]

print(testing.getConcatenation(example1))
print(testing.getConcatenation(example2))
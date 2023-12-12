class Solution (object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Given:
        - integer array of "nums"
        - return value is "ans"
        """

        """
        Goal:
        - We want to create array: ans
        - ans is a length of 2n, specifically
            Each element of nums maps onto ans
                nums[i] = ans[i]
            
            Each element of nums also maps at the end of list
            We basically map everything twice
                nums[i] = ans[i + n]
            
            Indicies are bounded [0, n)
                0 <= i < n
        """

        """
        Constraints:
            n is always the length of nums
                n == nums.length
            
            n is bounded [1,1000]
            This means we're gauranteed at least 1 element in nums
                1 <= n <= 1000
            
            The values of elements of n are bounded [1,1000]
                1 <= nums[i] <= 1000
        """ 

        """
        Two Ideas:
            Two loops of nums
            Two pointers to only loop once
        """

        """
        Two loops
        Spacetime: O(2n) for two loops
        Spacetime: O(2n) for ans

            Once to fill up the first half
            [1 2 1 _ _ _ ]

            Twice to fill up the rest
            [1 2 1 1 2 1 ]
        """

        """
        Two Pointers and one loop
        Runtime: O(n) | O(n) for loop, O(2) for updating values in ans
        Spacetime: O(n) | O(2n) for ans, O(1) for length, O(1) for pointer

            Since we know that n == nums.length
            We can use to pointers to fill everything up in one loop
            O(n)

            [ 1 _ _ 1 _ _ ]
            [ 1 2 _ 1 2 _ ]
            [ 1 2 1 1 2 1 ]

        1 Pointer solution
        Runtime: O(n) | O(2n + 2n) -> O(4n) 
        Spacetime: O(n) | O(2n + 1) 
        """

        #Array that will eventually grow to 2n
        #Spacetime: O(2n)
        ans = []

        """
        Total runtime: O(2n)
        Total spacetime: O(2n)
        """
        #Loop every value twice
        #Runtime: O(2), total runtime is O(2n)
        for i in range(2):
            #Runtime: O(n)
            for n in nums:
                #Assign the value to i and (i+length)
                #Runtime: O(1) 
                #Spacetime: O(1)
                ans.append(n)
        return ans

testing = Solution()
example1 = [4,5,6]
example2 = [10,55,88,90]

def printResults(example):
    #Prints our input and output
    print("Input array " + str(example))
    print("Output concetanted array:" + str(testing.getConcatenation(example)))
    print("")

printResults(example1)
printResults(example2)
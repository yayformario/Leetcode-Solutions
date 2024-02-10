class Solution (object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Constraints:
            Gauranteed between 1 and 100,000 entires
            1 <= nums.length <= 10^5
        
            Range of values are [-10,000,10,000]
                104 <= nums[i] <= 104
        """

        """
        Kadane's Algorithm:
        Runtime: O(n)
        Spacetime: O(1)

        Kadane's algorithm generally says to ignore negative sums when calculating largets sums
        - Negatives only hurt the Largest sum, so we can "skip" them 
        - For this problem, if a current subarray has a currentSum that's negative, we can ignore them
        - In practice, we can set the current sum to zero if it's ever negative
        - With a sharp eye, we either take (n + currentSum) or just (n) if currentSum is negative
        """

        #Initialize maxSum and currentSum
        maxSum = nums[0]
        currentSum = 0

        #Total runtime:O(n)
        #Loop entire array O(n)
        for n in nums:
            # Notice how we either take (n) on it's own or (n + current)
            # We usually take (n + current) UNLESS adding current makes it worse (Negative current sum) than just taking n alone
            # Essentially resets currentSum with (n) everytime currentSum becomes a negative sum
            currentSum = max(n, n + currentSum)

            #We want see if current Sum is larget than maxSum
            maxSum = max(maxSum, currentSum)

        return maxSum


#Create object 
testing = Solution()

examples = [
    #Given Examples
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8],

    #Single negative element example
    [-100],

    #Mix examples that needs resets
    [4,-1,2,-7,3,4],
    [60,-200,50,353,-100,-10,79,333],

    #All negatives example
    [-60,-200,-50,-353,-100,-10,-79,-333],
    [-3,-2,-3]
]

#Printing all examples
for n in examples:
    print("Example: " + str(n))
    print("Max Sum: " + str(testing.maxSubArray(n)))
    print("")
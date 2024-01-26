class Solution (object):
    #Brute force solution
    def bruteForce(self, nums):
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
        Bruteforce technique:
        Runtime: O(n^2)
        Spacetime: O(1)
            Maintaining maxSum and currSum

        - Essentially loop the entire array once O(n)
            - As we're looping, check every subarray for maxSum O(n)
            - For each iteration i, j checks length of current subarray
        - Total runtime is O(n * n)
        """

        # Since constraint can possible only have one value, we can initialize maxSum with first element
        maxSum = nums[0]

        #Total runtime: O(n^2)
        #Loops every element O(n)
        for i in range(len(nums)):
            #Initialize current sum for each subarray
            currentSum = 0
            #Loops every element of current subarray O(n)
            for j in range(i, len(nums)):
                currentSum += nums[j]
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
]

#Printing all examples
for n in examples:
    print("Example: " + str(n))
    print("Max Sum: " + str(testing.bruteForce(n)))
    print("")
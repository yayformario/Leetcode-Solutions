class Solution (object):

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

    def kadane(self, nums):
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
            #Check to see if current sum is larger than 0
            #If current sum is less than zero, it will only negatively affect the largest sum
            #We "restart" the largest sum by setting it zero
            currentSum = max(currentSum, 0)
            currentSum += n
            
            #--- Alternative: 
            #   Notice how we either take (n) on it's own or (n + current) after both operations
            #   We usually take (n + current) unless adding current makes it worse (Negative current sum) than just taking n alone
            #       currentSum = max(n, n + currentSum)

            #We want see if current Sum is larget than maxSum
            maxSum = max(maxSum, currentSum)

        return maxSum
    

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
    
    def maxSubArrayDivideAndConquer(self, nums):

        #Divide and conquer technique
        # We split a list in half
        #   Largest sum is in one of the three cases:
        #       Left max sum
        #       Right max sum
        #       Somewhere in the cross section

        #====----- Split the array -----===#
        #Get starting index, last index, and middle index
        start = 0
        end = (len(nums) - 1) 
        #start divide and conquer technique 
        return (self.divideAndConquer(nums, start, end))
        
    #Start and end are indicies
    def divideAndConquer(self, nums, start, end):
        #Base case is a single element, return that element
        #Single element means that both pointers are the same index
        if (start == end):
            return nums[start]

        #====----- Split the array -----===#
        #get the middle
        #Remember to use "//" in order to round down; division is decimal by default
        middle = (start + end) // 2

        #====----- Split the array -----===#
        
        #====----- Get left max sum -----===#
        #Left subarray is from: [start, middle]
        leftMax = self.divideAndConquer(nums, start, middle)

        #====----- Get right max sum -----===#
        #Right subarray is from [(middle + 1), end]
        rightMax = self.divideAndConquer(nums, (middle + 1), end)

        #====----- Get cross max sum -----===#
        crossMax = self.crossMax(nums, start, middle, end)

        #Get the max of all three and return that value
        return max(leftMax, rightMax, crossMax)

    def crossMax(self, nums, start, middle, end):
        #Keep track of current sum and maxSum
        currentSum = nums[middle]
        maxSum = currentSum

        #We need to store the indicies for the maxSum
        maxL = middle
        maxR = middle

        #Temp Pointer to crawl with
        temp = middle

        #We want to start at the middle index
        #From the middle index, crawl all the way to the left
        while temp != start:
            #Move temp pointer to the left
            temp -= 1

            #Update current sum
            currentSum += nums[temp]
            
            #Check if currentSum is larget than our maxSum
            if (currentSum > maxSum):
                #Update the maxSum
                maxSum = currentSum

                #Update the left pointer
                maxL = temp
        
        #Reset temp pointer and both sums, this time to crawl to the right
        temp = middle
        currentSum = nums[middle]
        maxSum = nums[middle]

        #From the middle index, crawl all the way to the right
        while temp != end:
            #Move temp pointer to the right
            temp += 1

            #Update current sum
            currentSum += nums[temp]

            #Check if currentsum is larger than our maxSum
            if (currentSum > maxSum):
                #Update maxSum 
                maxSum = currentSum
                maxR = temp

        #Reset maxSum
        maxSum = 0
        #Total sum for cross section is between maxL and maxR
        for i in range(maxL, (maxR+1)):
            maxSum += nums[i]

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
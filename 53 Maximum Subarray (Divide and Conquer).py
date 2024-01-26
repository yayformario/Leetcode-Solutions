class Solution(object):

    def maxSubArray(self, nums):

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

    
    

    

"""
Just to help visualize an example:
Splitting it in half until single elements
[-2,1,-3,4,-1,2,1,-5,4]
[-2,1,-3,4] [-1,2,1,-5,4]
[-2,1] [-3,4] [-1,2] [1,-5,4]
[-2] [1] [-3] [4] [-1] [2] [1] [-5,4]
[-2] [1] [-3] [4] [-1] [2] [1] [-5] [4]
#We reached our base cases
[-2] [1] [-3] [4] [-1] [2] [1] [-5] [4]

#then we want to 
"""
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
    print("Max Sum: " + str(testing.maxSubArray(n)))
    print("")
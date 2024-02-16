class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """    
        #Initialize return value
        returnValue = 0
        
        #Two pointer approach
        #Left pointer will slide with window
        leftPointer = 0
 
        currentSum = 0
        currentAvg = 0

        #Loops entire array O(n)
        for rightPointer in range (len(arr)):
            currentSum += arr[rightPointer]
            currentAvg = currentSum // k

            #Grow window until size k
            if ((rightPointer - leftPointer + 1) == k):
                if (currentAvg >= threshold):
                    returnValue += 1
                #Our window is at size k
                #incremeneting L now will gaurantee that we stay at k next iteration
                currentSum -= arr[leftPointer]
                leftPointer += 1

        return returnValue

testing = Solution()

examples = [
    #Given examples: arr, k, threshold
    [2,2,2,2,5,5,5,8], 3, 4, #expecting 3
    [11,13,17,23,29,31,7,5,2,3], 3, 5, #Expecting 6

    #One element & threshold 0 case
    [10],1,0, #expecting 1

    #Threshold exceeding maximum array average
    [10],1,11, #expecting 0
    
]

for i in range(0, len(examples), 3):
    print(
        "Input: " + str(examples[i]) +
        "\tK: " + str(examples[i+1]) +
        "\tThreshold: " + str(examples[i+2]) + 
        "\n" +
        "Output: " + str(testing.numOfSubarrays4(examples[i], examples[i+1], examples[i+2]))
    )

"""
Restrictions:
At least one element in arr
No negatives; no zeros
k is at least 1 and can't be bigger than arr.length
threshold can be zero
"""
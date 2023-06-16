class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """    

        #Given threshold and window size (k)
        
        #Avg = (sum) // (number of elements)
        #Avg = (sum) // (k)
        #   Avg >= Threshold | Threshold <= Avg
        #Threshold <= (sum) // (k)
        #Threshold * k <= sum
        #Sum >= Threshold * k <--- all we have to do is crawl the window while calculating sum

        #Initialize condition, currSum, and count
        condition = threshold * k
        currSum = 0
        count = 0

        #Initialize L pointer to keep track of window size

        #R will crawl entire array
        for R in range(len(arr)):
            #Update currSum
            currSum += arr[R]

            #Check if window size is too big
            if ((R-L+1) > k):
                #update currSum and move L
                currSum -= arr[L]
                L +=1

                #This will mean that our window size is now size k, check if we can increment count
                if (currSum >= condition):
                    count += 1

        return count

testing = Solution()

example = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(testing.numOfSubarrays(example, k, threshold))

example = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(testing.numOfSubarrays(example, k, threshold))

example = [11,13,17,23,29,31,7,5,2,3]
k = 1
threshold = 2
print(testing.numOfSubarrays(example, k, threshold))

example = [11,13,17,23,29,31,7,5,2,3]
k = 1
threshold = 31
print(testing.numOfSubarrays(example, k, threshold))

example = [11,13,17,23,29,31,7,5,2,3]
k = 2
threshold = 5
print(testing.numOfSubarrays(example, k, threshold))

example = [11]
k = 3
threshold = 5
print(testing.numOfSubarrays(example, k, threshold))

example = [11]
k = 1
threshold = 5
print(testing.numOfSubarrays(example, k, threshold))

example = [12]
k = 1
threshold = 12
print(testing.numOfSubarrays(example, k, threshold))

example = [11]
k = 1
threshold = 12
print(testing.numOfSubarrays(example, k, threshold))

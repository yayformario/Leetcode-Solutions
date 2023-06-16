class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """    
        #Sliding Window Approach
        
        #Initialize two pointers
        L = 0
        R = 0

        #Initialize average, sum, and count
        avg = 0 
        currSum = 0 
        count = 0
            
        #Now we crawl window until end of array (if we haven't already hit it)
        while (R < len(arr)):
            #update currSum and avg
            currSum += arr[R]
            #Divide by k since the window will always be size of k
            avg = (currSum // k) #rounded down to avoid decimals 

            #Only do comparisons once we have our window size
            if ( (R-L+1) == k):
                #check if this subarray >= threshold
                if (avg >= threshold):
                    count += 1
                #Crawl window by decrmenting sum and moving L
                currSum -= arr[L]
                L += 1
            
            #Increment R
            R += 1


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
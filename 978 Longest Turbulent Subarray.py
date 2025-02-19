class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        #Helper function for signs
        def helper(L,R):
            # (<) == -1
            # (>) == 1
            # (=) == 0
            sign = 0

            if (L < R):
                sign = -1
            elif (L > R):
                sign = 1

            return sign
         
        #Kadane / Sliding Window Approach: O(n)

        #Check for single elements
        if (len(arr) == 1):
            return 1
        
        #initialize counter and maxTurb
        counter = 1
        maxTurb = 1

        #initialize prevSign and pointers
        prevSign = None
        R = 1

        #R loops entire array: O(n)
        while R < len(arr):
            #get currentSign
            currentSign = helper((arr[R-1]), arr[R])

            #Check if previous sign was "="
            if (prevSign == 0):
                prevSign = currentSign # Update prevSign from "=" as soon as possible

            #Check for resets
            if( (prevSign == currentSign) or (currentSign == 0)):
                maxTurb =  max(maxTurb, counter)
                counter = 1
                if (currentSign == 0):
                    #Edge case: [8,8] = 1
                    #Hard reset to zero because "=" is not a turbulent sign;  a new "block"
                    counter = 0

            #Increment by default every iteration and update maxCounter as needed
            counter += 1
            maxTurb = max(maxTurb, counter)

            #Update previous sign and increment
            prevSign = currentSign
            R += 1
            
        return maxTurb
    
    def maxTurbulenceSize2(self, arr):
        """
        Constraints:
            Length: [1, 10000]
            elements range: [0,1000000000] // no negatives
        Edge cases: 
            One element
                return 1
        """
        #Default value
        maxTurb = 1 
        currentTurb = 1

        #equal sign: 0
        #greater than: 1
        #less tha: -1
        prevSign = 0
        currentSign = 0

        #Can safely search (i+1) without going out of bounds
        for i in range(len(arr) - 1):
            
            #===----- Update the currentSign  -----===#
            #If nextValue is the same value
            if (arr[i] == arr[i+1]):
                currentSign = 0
            #If next value is greater than
            elif (arr[i] > arr[i+1]):
                currentSign = 1
            #If next value is less than
            elif (arr[i] < arr[i+1]):
                currentSign = -1

            #===----- Compare the signs for turb -----===# 
            #Three cases: 
            #IMPORTANT TO CHECK IF CURRENTSIGN == 0 FIRST
            # currentSign == 0; reset currentTurb to 1
            if (currentSign == 0):
                maxTurb = max(maxTurb, currentTurb)
                currentTurb = 1
            # currentSign == prevSign; reset currentTurb to 2
            elif (currentSign == prevSign):
                maxTurb = max(maxTurb, currentTurb)
                currentTurb = 2
            
            # currentSign != prevSign; increment currentTurb 
            elif (currentSign != prevSign):
                currentTurb += 1
                maxTurb = max(maxTurb, currentTurb)

            #===----- Update prevSign -----===# 
            prevSign = currentSign
            
        return maxTurb
    

testing = Solution()
example = [9,4,2,10,7,8,8,1,9]
print(testing.maxTurbulenceSize(example))

example = [4,8,12,16]
print(testing.maxTurbulenceSize(example))

example = [100]
print(testing.maxTurbulenceSize(example))

example = [100,100]
print(testing.maxTurbulenceSize(example))

example = [1,2,3,4,5]
print(testing.maxTurbulenceSize(example))

example = [10,9,8,7,6,5,4,3,2,1]
print(testing.maxTurbulenceSize(example))

example = [8,8,8,8,8,8,8,8,8]
print(testing.maxTurbulenceSize(example))

example = [2,2,2,5,1,10,10,3,2,6,8,4,5,6,6,12,11,10,3,2,1,1]
print(testing.maxTurbulenceSize(example))

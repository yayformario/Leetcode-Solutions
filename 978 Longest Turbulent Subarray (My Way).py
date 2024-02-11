class Solution (object):
    def maxTurbulenceSize(self, arr):
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

examples = [
    #Given examples
    [9,4,2,10,7,8,8,1,9],
    [4,8,12,16],
    [100],

    #Failed test case: expected 8
    [0,8,45,88,48,68,28,55,17,24],

    #Single value test case: Expected 1 
    [1],
    
    #All same sign test case: Expected 2
    [0,1,2,3,4,5,6,7,8,9],

    #All different sign test case: Expected (n)
    [0,99,1,98,2,97,3,96,4,95], #Expected 10
    
    #All same value test case: Expected 1
    [12,12,12,12,12,12,12,12,12,12], 

    # Mixed case
    [120,852,456,951,753,654,123,987,1,2,3,4,5,69,8,7,4,5,6,3,2,1]
]

for ex in examples:
    print("Example: " + str(ex) + "\nOutput: " + str(testing.maxTurbulenceSize(ex)))

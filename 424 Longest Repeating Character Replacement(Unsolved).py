class Solution(object):
    def characterReplacement(self, s, k):
        #Return value
        maxLen = 0

        #Two Pointer approach
        leftPointer = 0
        replaceCount = 0

        #Going to need a hashmap
        charCounters = {}

        #We can initialie it with the first letter and a counter of zero
        charCounters[s[0]] = 0
        
        #Keep track of the most re-ocurring character
        maxOccurence = 0
        #Loop entire array:
        for rightPointer in range(len(s)):
            #Check if letter in hashmap
            if (s[rightPointer] in charCounters):
                #Incrementer letter counter
                charCounters[s[rightPointer]] = charCounters[s[rightPointer]] + 1
                maxOccurence = max(maxOccurence, charCounters[s[rightPointer]])
                
            #Not in hashmap
            else:
                #Add the letter to our hashmap
                charCounters[s[rightPointer]] = 1
            
            #[maxOccurenece + k] the largest window we can have
            #We update maxLen as long as <= than that
            if ((rightPointer - leftPointer + 1) <= (maxOccurence + k)):
                    maxLen = max(maxLen, rightPointer - leftPointer + 1)
            
            
            #Shrink window if it's too long for replacements
            if ((rightPointer - leftPointer + 1) > (maxOccurence + k)):
                #If L is the max occuring char, decrement maxOccurence
                if (charCounters[s[leftPointer]] == maxOccurence):
                    maxOccurence -= 1
                #Decrement hash value
                charCounters[s[leftPointer]] = charCounters[s[leftPointer]] - 1

                #Move left pointer
                leftPointer += 1



        return maxLen
    

testing = Solution()

examples = [
    "BCDAA", 1, #expecting 3
    "AABABBA", 1, #expecting 4
    "ABAB", 2, #expecting 4
    

    #k is zero test case
    "ABCD", 0, #expecting 1
    "EEEE", 0, #expecting 4 
    "ABCDD", 0, #expecring 2

    #k == len case, return value is always len
    "ABCDEFG", 7,  #expecting 7

    #Long middle answer"
    "ABBCDEFGHHHHJJJKKKKLMOP", 3, #expecting 7

    #half and half
    "AAAABBBB", 2 #Expecting 6


    
]

for i in range(0, len(examples), 2):
    print(
        "String: " + str(examples[i]) +
        "\tk = " + str(examples[i+1]) + 
        "\nOutput: " + str(testing.characterReplacement(examples[i], examples[i+1]))
    )
"""
Notes:

Constraints:
Gauranteed a length of 1
ONLY capital english letters
k can be zero, k maxes out at length of string
"""
class Solution(object):
    def characterReplacement(self, s, k):
        #Return value
        maxLen = 0

        #Two Pointer approach
        leftPointer = 0
        replaceCount = 0
        #Going to need a hashmap
        
        #Loop entire array:
        for rightPointer in range(len(s)):
            #Check if we find a new character
            if (s[leftPointer] != s[rightPointer]):
                replaceCount += 1
                #Slide window to ensure we have enough
                if (replaceCount > k):
                    leftPointer += 1
                    replaceCount -= 1
            maxLen = max(maxLen, (rightPointer - leftPointer + 1))
        return maxLen
    

testing = Solution()

examples = [
    #Given examples
    "ABBCDEFGHHHHJJJKKKKLMOP", 3,
    "ABAB", 2, #expecting 4
    "AABABBA", 1, #expecting 4

    #k is zero test case
    "ABCD", 0, #expecting 1
    "EEEE", 0, #expecting 4 
    "ABCDD", 0, #expecring 2

    #k == len case, return value is always len
    "ABCDEFG", 7,  #expecting 7

    #Long middle answer"
    "ABBCDEFGHHHHJJJKKKKLMOP", 3 #expecting 4


    
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
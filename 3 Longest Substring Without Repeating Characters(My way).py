class Solution(object):
    def lengthOfLongestSubstring(self, s):

        #Sliding Window approach 
        leftPointer = 0

        #Hash to search for duplicate
        uniqueChars = set()

        #Keept track of lengths
        maxLength = 0

        for rightPointer in range(len(s)):
            #Slide window until duplicate has been removed
            while s[rightPointer] in uniqueChars:
                
                uniqueChars.remove(s[leftPointer])
                #Move left pointer to the current position
                leftPointer += 1 

            #Add the char to our set
            uniqueChars.add(s[rightPointer])

            #Update max length as needed
            #Current length is size of window: R - L + 1
            maxLength = max(maxLength, rightPointer - leftPointer + 1)

        return maxLength
    
testing = Solution()

examples = [
    #given examples
    "abcabcbb", #expecting 3
    "bbbbb", #expecting 1
    "pwwkew", #expecting 3

    #Empty list 
    "", #Expecting 0
    #Letter
    "a", #expecting 1
    #Number
    "0", #expecting 1
    #symbol
    "$", #expecting 1
    #space
    " ", #expecting 1
    #reset in the middle
    "dvdf", #expecting 3
    #Larger right half than left half
    "12345aa67890 " #expecting 7
]

for ex in examples:
    print(
        "Input: " + str(ex) +
        "\nOutput: " + str(testing.lengthOfLongestSubstring(ex)) +
        "\n"
    )

"""
Notes:

Constraints:
We can expect a length of zero, empty string
String consists of english letters, digits, symbols, and spaces
"""
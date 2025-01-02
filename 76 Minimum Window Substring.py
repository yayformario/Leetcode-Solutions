class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Early exit cases
        if len(t) < 1:
            return ('')
        if len(t) > len(s):
            return ('')
        
        #Initialize hashes and counter for matches
        hashT = {}
        hashWindow = {}
        matches = 0

        #Initialize pointer
        left = 0

        #Initialize smallest window pointers
        smallestLeft = 0
        smallestRight = 0
        smallestWindow = len(s) + 1

        #Hash t
        for char in t:
            hashT[char] = hashT.get(char, 0) + 1
        
        #Loop string S; Grow window until we find 't'
        for right in range(len(s)):
            #Store char for readability
            char = s[right]
            #Increment or add to hash
            hashWindow[char] = hashWindow.get(char, 0) + 1

            #Chech if char is also in our hashT
            if char in hashT:
                #If it is, check if there's an idneitcal amount of counters
                if hashWindow[char] == hashT[char]:
                    #Then it's a match
                    matches += 1

            #Once all matches have been found; shrink the window if possible
            if matches == len(hashT):
                while matches == len(hashT):
                    #storing vars for readability
                    leftChar = s[left]

                    #Update smallestWindow as needed
                    if smallestWindow > right-left+1:
                        smallestLeft = left
                        smallestRight = right
                        smallestWindow = right-left+1


                    #Decrement or remove from hash
                    if hashWindow[leftChar] == 1:
                        hashWindow.pop(leftChar)
                    else:
                        hashWindow[leftChar] -= 1
                    
                    #Check to see if we shrunk too much
                    if leftChar in hashT:
                        if hashT[leftChar] > hashWindow.get(leftChar,0):
                            matches -=1
                    left+=1
        
        if smallestWindow == len(s) + 1:
            return ('')
        
        #initialize return string
        returnString = ''

        for i in range(smallestRight - smallestLeft + 1):
            returnString += s[smallestLeft + i]

        return (returnString)
    
    
    
testing = Solution()

#Recall: 't' has to be inside of 's' for a solution
testCases = [
    #[s,t]
    #Given
    ["ADOBECODEBANC","ABC"], #returns 'BANC'
    ['a','a'], # returns 'a'
    ['a','aa'], # returns ''

    #Early exits cases: T is empty or T > S
    #T is empty
    ['a', ''],
    #T > S
    ['abc', 'abca'],

    #Case sensitive 
    ['A','a']
]

for case in testCases:
    print('return value: ' + str(testing.minWindow(case[0],case[1])) + '\n')
class Solution(object):
    """
    Add all letters and their count into a hashmap
    Compare hashmaps to see if they're identical

    Runtime: O(2n) (Loops both strings at the same time and then compares the two hashmaps)
    Spacetime: O(2n) (Need two hashmaps of size n)
    """
    def isAnagram(self, s, t):
        returnValue = False

        #If not same length, return False
        if (len(s) != len(t)):
            return returnValue
        
        #Create a hashmap for each string
        hashMapS = {}
        hashMapT = {}

        #Increment both hashmaps at the same time
        for i in range(len(s)):
            #If already in hashmap, increment the counter
            if s[i] in hashMapS:
                hashMapS[s[i]] = hashMapS[s[i]] + 1
            #If not in hashmap, add it to hashmap
            else: 
                hashMapS[s[i]] = 1

            #Do the same thing for string t
            if t[i] in hashMapT:
                hashMapT[t[i]] = hashMapT[t[i]] + 1
            else: 
                hashMapT[t[i]] = 1

        #We now want to compare both hashmaps
        #In this case, we'll convert them to strings and then compare
        if (hashMapS == hashMapT): 
            return True 

        return returnValue
    
testing = Solution()

examples = [
    
    #Given examples
    "anagram", "nagaram", #true
    "rat", "car", #false

    #One length examples
    "a", "a", #True
    "m", "n", #false

    #Different size examples
    "abc", "de", #false
    "qwerty", "qwertyu", #false

    #Same size, not anagrams"
    "asdfg", "asdfc", #false 
    "ss", "qq" #false

]

for i in range(0, len(examples), 2):
    print(
        "s: " + str(examples[i]) +
        "\tt: " + str(examples[i+1]) +
        "\nOutput: " + str(testing.isAnagram(examples[i], examples[i+1])) + "\n"
    )

"""
Notes:
Going to try a hash solution. 

If sizes aren't the same, return False

If sizes are the same, there's a handful of different approaches:
    
    #===----- Approach 1 -----===# 
    Create two hashes and compare them. 

        Runtime: O(2n) (Loops both strings at the same time and then compares the two hashmaps)
        Spacetime: O(2n) (Need two hashmaps of size n)
            1 hashmap for each string, compare 2 the hashmaps to see if they're equal
        
        Note:   This was a gamble for me because I wasn't sure if comparing two hashmaps
            was sensitive to the keys/values being in order or not. 
                If it wasn't sensitive to inorder; then it's perfect, we can just compare them
                If it was sensitive to inorder; then it's useless since we have to sort keys/values
                    Best sorting algos are already nlogn and we're back to square one


    #===----- Approach 2 -----===# 
    1 hashmap for both strings, increment hashmap for s, decrement hashmap for t 
    
        Runtime: O(2n) (Loop once for s, loop again for t)
        Spacetime: O(n) (only need one hashmap of size n)
            
            After looping through t, there are only three cases:
                if hashmap is empty at the loops; it's an anagram
                if it's not empty; it's not an anagram
                if t[i] doesn't exist in hashmap; it's not an anagram
    
    #===----- Approach 3 -----===# 
    1 hashmap for both strings, increment for both s and t
        
        Runtime: O(2n) (One loop to add both strings, one loop to for every hash)
        Spacetime: O(n) (only need one hashmap of size n)
            if each entry is divisible by 2, then it's an anagram

        Note: WON'T WORK; THE LOGIC IS WRONG
        Sharing one hashmap makes it difficult to tell which letter came from where
        EDGE CASE:
            s = "aa", t = "bb"
                
                This would take into account: "ab" "ab" and "ba" "ba"
                But unfortunately also takes into account: "aa" "bb" and "bb" "aa"
            
Constraints:
Both are gauranteed to be at least of length 1
Both only include lowercase english letters (26 unique characters worst case)
"""
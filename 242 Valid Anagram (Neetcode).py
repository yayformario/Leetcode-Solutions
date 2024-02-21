class Solution:
    def isAnagram(self, s, t):
        #If not same length, return False
        if len(s) != len(t):
            return False
        
        #Hashmap for both strings
        countS = {}
        countT = {}

        #O(n)
        for i in range(len(s)):
            #Take advantage of the .get(key, default) call 
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        #Returns True if the hashmaps are the same
        #Returns False if the hashmaps are not the same; not an anagram
        return countS == countT
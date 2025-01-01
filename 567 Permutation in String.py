class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        #Left pointer for window slide 
        left = 0
        windowSize = len(s1)
        s1Hash = {}
        windowHash = {}

        for char in s1:
            if char in s1Hash:
                s1Hash[char] += 1
            else:
                s1Hash[char] = 1
        
 
        #Outerloop that grows window, starts at 'window'
        for right in range(len(s2)):
            #Slide window if it's too large
            if right-left+1 > windowSize:                
                if windowHash[s2[left]] > 1:
                    windowHash[s2[left]] -= 1
                else:
                    windowHash.pop(s2[left])
                    
                
                left +=1

            #Update hash as window slides
            if s2[right] in windowHash:
                windowHash[s2[right]] += 1
            else:
                windowHash[s2[right]] = 1

            if windowHash == s1Hash:
                return True

        return False
    

testing = Solution()
tests = [
    ['adc', 'dcda'],
    ['ab', 'eidboaoo'],
    ['ccc', 'cbac']
]

for test in tests:
    testing.checkInclusion(test[0], test[1])
        
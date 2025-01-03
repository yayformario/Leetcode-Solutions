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
            #hash example; essentially in this example it's if char else 0
            s1Hash[char] = s1Hash.get(char,0)+1

        #Outerloop that grows window, starts at 'window'
        for right in range(len(s2)):
            #Slide window if it's too large
            leftChar = s2[left]
            if right-left+1 > windowSize:                
                if windowHash[leftChar] > 1:
                    windowHash[leftChar] -= 1
                else:
                    windowHash.pop(leftChar)

                left +=1

            #Update hash as window slides
            rightChar = s2[right]
            windowHash[rightChar] = windowHash.get(rightChar,0) + 1

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
        
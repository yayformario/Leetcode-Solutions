class Solution:
    #Trick is skipping non alphanumeric input
    #gauranteed at least 1 letter
    def isPalindrome(self, s: str) -> bool:
        #Quick exit
        length = len(s)
        if length == 1:
            return True
        
        #Two pointer solution
        left = 0
        right = length-1

        while left < right:
            #Only compare the alphanumeric values
            while not (s[left].isalnum()) and left < right:
                left+=1
            while not (s[right].isalnum()) and left < right:
                right-=1

            #Edge case: All special character results in an empty string
            #Empty strings are apparently palindromes :^)
            if left==right:
                return True
            
            #Guaranteed alphanumeric
            #Easier to check for cases that aren't palindrome

            # letter and num
            leftNum = s[left].isnumeric()
            leftChar = s[left].isalpha()
            rightNum = s[right].isnumeric()
            rightChar = s[right].isalpha()

            #False if: both aren't num or letter
            bothNums = leftNum and rightNum
            bothChars = leftChar and rightChar
            
            #Direct compare if both nums are the same value
            if bothNums == True:
                if s[left] != s[right]:
                    return False
                left +=1
                right -=1
            
            #lowercase the letter then compare them
            elif bothChars == True:
                if s[left].lower() != s[right].lower():
                    return False
                left +=1 
                right -=1
            else:
                return False
                        
        return True
    
testing = Solution()

input = [

    #Missed edge cases: all special chars
    #All are non-alphanumerics are 'True' because they reduce to '' :^)
    #Empty string is apparently a palindrome :^)
    '.,' #True 
    "!@#$%^", #True;

    #Given examples
    "A man, a plan, a canal: Panama", #True
    "race a car", #false
    " ", #true

    #All nums
    "000111000", #True
    
    #All chars
    "RACECAR",

    #Nums and letters
    "a1", #false
    "2b", #false

]

for example in input:
    print(str(testing.isPalindrome(example)))
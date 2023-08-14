class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        Only given the following characters:
            '()[]{}'

        An input string is valid if:
            Open brackets must be closed by the same type of brackets
            Open brackets must be closed in the correct order
            Every close bracket has a corresponding open bracket of the same type
        """

        
        """
        Stack and Hashmap approach
        """
        
        #Create an empty stack to track parenthesis
        stack = []

        #Hashmap
        #   Key: Closing Brackets
        #   Value: Open Brackets
        myMap = {")":"(" , "]":"[", "}":"{"}

        #Loop entire string
        for bracket in s:
            #Search for Open Brackets
            if bracket not in myMap:
                stack.append(bracket)
                continue
            if not stack or stack[-1] != myMap[bracket]:
                return False
            stack.pop()


        #return true by default
        return not stack
        

testing = Solution()

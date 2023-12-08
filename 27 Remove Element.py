class Solution (object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        """
        Given:
            nums - integer array
            val - integer
            k - number of elements in nums not equal to val 
            return - k
        """

        """
        To get accepted:
        - Change array in nums such that:
            - First "k" elements contain elements not equal to val
            - Remaining elements of nums are not important
                -Must also be size of nums
        """

        """
        Edge Cases:
            Entire array doesn't include the val
                - Returns the entire array
            
            Entire array composed of val:
                - Returns 0, no elements exists

        Visual Case: 
            Entire array only has 1 value NOT val:
                - Returns 1, since 1 value didn't match and L was incremeneted
            
        Since there's the possibility of:
            Returning 0 elements
            L starts on 0
            No need to offset where we return 0 elements and L doesn't move
            
            Return (L)
        """

        """
        Two pointer approach
        Runtime: O(n) 
        SpaceTime: O(1) | L and R index

        Idea:
        - L and R start at first element
        - R loops entire array
        - L only increments if (R != val)
        """

        #L index | O(1) spacetime
        L = 0
        #R pointer will loop entire array O(n)
        for R in nums:
            """
            Instinctually, I want to start with checking to see if R equals val:
                R == val
                    But since we want to skip val if it pops up, 
                    we don't really do anything here
            
            So I eventually deduce that we only care about the times R doesn't equal val:
                R != val
            """
            #Check to see if current value DOES not equal nums O(1)
            if R != val:
                #Save this value at current index L O(1)
                nums[L] = R
                
                #Increment the L Pointer O(1)
                L += 1
        
 
        # No need to offset. Edge case: return 0 elements and L doesn't move
        return L

testing = Solution()

example1 = [3,2,2,3]
val1 = 3

example2 = [0,1,2,2,3,0,4,2]
val2 = 2

#Edge case where entire array doesn't include the val
example3 = [5,6,7,2,5,1,4]
val3 = 0

#Edge case where entire array array composed of val
example4 = [9,9,9,9,9,9,9]
val4 = 9

#Visual case where entire array only has 1 value NOT val
example5 = [8,7,6,4,2,2,1,0,1,9,4]
val5 = 6

print(testing.removeElement(example1, val1))
print(testing.removeElement(example2, val2))
print(testing.removeElement(example3, val3))
print(testing.removeElement(example4, val4))
print(testing.removeElement(example5, val5))
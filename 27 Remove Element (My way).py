class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        

        """
        Given the following 
        - nums: integer array
        - val: integer
        - K: Return value. Number of elements in nums which are not equal to val
        """

        """
        Goal
        - Remove all occurences of val in nums 
        - Must be done in place
        """

        """
        To get accepted:
        - Change nums such that first k elements of nums are all not equal to val
        - Remaining elements of nums are not important
        - Size of nums not important

        """

        """
        Constraints: 
        The length of nums can be zero but no more than 100.
        - 0 <= nums.length <= 100
        
        The value of elements are between 0 and 50 inclusive
        - 0 <= nums[i] <= 50

        The value of given to us is between 0 and 100 inclusive
        - 0 <= val <= 100
        """

        """
        Things to note:
        - Order of elements may be changed
        - Values that are 51 to 100 will never be in the list of nums
        - We can potentially be given an empty list
        """

        #Check for empty list; easy optimization [O(1)]
        if len(nums) == 0:
            #List has no elements; thus we return 0
            return 0

        #Check to see if val is greater than 50 [O(1)]
        if val > 50:
            #val will NEVER be in nums
            #return length of nums. O(1)
            return len(nums)
        
        """
        At this point:
        - We're gauranteed at least 1 element in nums
        - Val can potentially appear in nums
        """

        """
        Two Pointer approach:
        - R crawls entire list of nums
        - L crawls when we find an element NOT equal to val

        If nums[R] == val:
            R crawls
            L does not crawl

        if nums[R] != val:
            R crawls
            L crawls by 1
            nums[L] gets updated with nums[R]

        NOTE: 
        L and R start at the same index
        That means on the first loop that nums[L] == nums[R]
            L doesn't crawl if: nums[R] == val 
                L returns zero if it was the only element to check

            L gets updated regardless for consistency of algorithm
            This is the only case of redundant work O(1)
                nums[L] == nums[R]

            L then crawls forward to prep for next unique value
        """

        """
        Edge cases:
        What if none of the values are val?
            L crawls everytime R crawls: O(2n)
            This makes len(nums) == L
            We want to return len(nums)
            Thus can also return L
        
        What if all the values are val?
            L never crawls as R loops entire list: O(n)
            Since L == 0, we return L

        Our return value for all cases should be L
        """
        #Create pointer for L. [O(1) spacetime]
        L = 0

        #Loop entire nums [O(n)]
        #element essentially acts as nums[R]
        for element in nums:
            #Since L doesn't crawl if element == val
            #We want to look for cases where element != val
            if element != val:
                #Update unique value [O(1)]
                nums[L] = element

                #Crawl L pointer to prep for next value [O(1)]
                L += 1

        #return value is L, check "Edge cases" for explanation
        return L

#Create a solution object for testing
testing = Solution()

#Given examples
nums1 = [3,2,2,3]
val1 = 3

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2

#Empty list edge case
nums3 = []
val3 = 10

#vals > 50 edge case
#Constraint: 0 <= nums[i] <= 50
nums4 = [0,1,2,3,4,5,6,50]
val4 = 51

#None of nums[i] equal val edge case
nums5 = [50,28,12,0,13,44]
val5 = 1

#All of nums[i] equal val edge case
nums6 = [7,7,7,7,7,7,7,7]
val6 = 7


#Function that prints input and output
def printResults(nums, val):

    #Return
    print("Test Case:")
    print("nums = " + str(nums))
    print("val = " + str(val))

    #Get the return value
    k = testing.removeElement(nums,val)
    print("Return value k: " + str(k))
    print("List without val filtered data:")
    print(nums[0:k])
    print("List without val raw data:")
    print(nums)
    print("")

#Print results:
printResults(nums1,val1)
printResults(nums2,val2)
printResults(nums3,val3)
printResults(nums4,val4)
printResults(nums5,val5)
printResults(nums6,val6)

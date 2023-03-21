class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        #Fixed Sliding Window Approach: O(n)

        #initialize hashset to detect duplicate
        window = set()

        #Two Pointer approach
        L = 0
        
        #R index crawls entire array: O(n)
        for R in range(len(nums)):
            #Slide window when needed (if larger than k requirement)
            if ( (R-L) > k):
                #Slide by removing L from our hashset and incrementing L 
                window.remove(nums[L])
                L += 1

            #Check to see if R is in our hashset
            if nums[R] in window:
                return True

            #Add R's value to hashset
            window.add(nums[R])

        #If we made it to the end without finding duplicate, return false
        return False

testing = Solution()
example = [1,2,3,1]
k = 3
print(testing.containsNearbyDuplicate(example, k))


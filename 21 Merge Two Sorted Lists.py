from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    
class Solution:

    def printLinkedList(self, list):
        traverse = list
        arr = []


        while traverse:
            arr.append(traverse.val)
            traverse = traverse.next

        
        print(arr)
            

    def linkedListConverter(self, array):
        #first element is the head
        head = ListNode()
        head.val = array[0]

        #The rest of the elements get linked
        traverse = head
        for i in range(1,len(array)):
            temp = ListNode()
            temp.val = array[i]

            traverse.next = temp
            traverse = temp

        return head
            
    
 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #Quick exits: empty lists
        if not list1 and not list2:
            return list1
        
        if not list1 or not list2:
            if not list1:
                return list2
            else:
                return list1
            
        #Guaranteed two lists
        if list1.val > list2.val:
            smallerVal = list2
            largerVal = list1
        else:
            #list1 is smaller or equal
            smallerVal = list1
            largerVal = list2

        #Store the head of the smallest list value
        head = smallerVal

        #Gauranteed two linked lists at this point
        while smallerVal and largerVal:

            """
            Always need to crawl up

            Determine if we need to adjust pointers before crawling up

            Don't need to adjust pointers when:
                next.val exists
                next.val < largerVal
            
            """
            #Check if
            if smallerVal.next:
                if not (smallerVal.next.val > largerVal.val):
                    #attach current value to head
                    smallerVal = smallerVal.next
                else:
                    #We can crawl upwards
                    temp = smallerVal.next
                    smallerVal.next = largerVal
                    smallerVal = temp



            else:
                #We can crawl upwards
                temp = smallerVal.next
                smallerVal.next = largerVal
                smallerVal = temp

            #might need to flip values after each iteration
            if smallerVal and largerVal:
                #flip lists if new smallerValue is larger
                if smallerVal.val > largerVal.val:
                    #Flip them
                    temp = largerVal
                    largerVal = smallerVal
                    smallerVal = temp
                    

    
        return head
            


            
            
"""
Edge cases:
Both lists are empty
1 list is empty
even lists
uneven lists
1 list is larger than the other
lists have multiple of same value
lists are identical (unique values)
"""
examples = [
    
    #Both lists are empty
    [ [], [] ],

    #1 list is empty
    [ [], [0] ],
    [ [0], [] ],

    #One element lists
    [ [1] , [1] ],
    [ [1] , [2] ],
    [ [2] , [1] ],

    #even lists
    [ [1,2], [3,4]],



    #uneven lists
    [ [4,5,6],[1,2] ], 

    #1 list is larger than the other
    [ [7,8,9], [1,2,3]],

    #lists have multiple of same value
    [ [1,1,1,1] , [1,1,1,1] ],

    #lists are identical (unique values)
    [ [1,2,3], [1,2,3] ],

    #'sandwhich' list
    [ [20,21,22],[1,100] ],
    [ [1,2,4], [1,3,4] ],

]

testing = Solution()
#loop each solution
for ex in examples:
    list1 = None
    list2 = None


    #Only convert if not empty
    #initialize head
    if ex[0]:
        list1 = testing.linkedListConverter(ex[0])

    if ex[1]:
        list2 = testing.linkedListConverter(ex[1])

    head = testing.mergeTwoLists(list1, list2)
    testing.printLinkedList(head)
    











    
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

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
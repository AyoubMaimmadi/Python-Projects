class ListNode:
    def init_(self, val=0, next=None) :
        self.val = val
        self.next = next

class Solution :
    def removeElements (self, head: ListNode, val: int) -> ListNode :
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            nxt = curr.nxt
            if curr.val == val:
                prev.next = nxt 
            else:
                prev = Curr
                
            Curr= nxt
        return dummy.next



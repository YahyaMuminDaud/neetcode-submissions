# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        a = []
        b = []
        curr = head

        while curr:

            a.append(curr.val)
            curr = curr.next
        
        i = 0
        j = len(a) - 1

        while i < len(a) - 1:
            
            if i >= j:
                break
            b.append(a[i])
            b.append(a[j])
            i += 1
            j -= 1
        
        if i == j:
            b.append(a[i])
        
        new = head
        k = 0
        while new:

            new.val = b[k]
            k += 1
            new = new.next
        
        
# Last updated: 6/6/2026, 10:27:22 PM
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # self.list1=None 
        # # curr =list1
        # while curr.next!=None:
        dummy=ListNode(-1)
        curr=dummy

        while list1 is not None and list2 is not None:
            if list1.val <list2.val:
                curr.next=list1
                list1=list1.next 
            else:
                curr.next=list2
                list2=list2.next 
            curr=curr.next
        
        if list1 is not None:
            curr.next=list1 
        else:
            curr.next=list2
        return dummy.next






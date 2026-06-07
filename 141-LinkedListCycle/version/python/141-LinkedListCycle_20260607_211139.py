# Last updated: 6/7/2026, 9:11:39 PM
1class Solution:
2    def hasCycle(self, head: Optional[ListNode]) -> bool:
3        fast=head
4        slow=head
5        # flag =True 
6
7        while fast and fast.next:
8            slow=slow.next 
9            fast =fast.next.next
10            # curr =curr.next 
11            if slow==fast:
12                return True 
13
14        return False  
15
16        
17
18
19
20        
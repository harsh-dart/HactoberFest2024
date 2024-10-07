#problem Link: https://leetcode.com/problems/reverse-nodes-in-k-group/description/
class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return head
        
        cur = head
        prev = None
        ne = head.next
        
        # Check if there are k nodes left
        for i in range(k - 1):
            if not ne:
                return cur
            ne = ne.next
        
        ne = head.next
        
        # Reverse k nodes
        for i in range(k):
            cur.next = prev
            prev = cur
            cur = ne
            if not ne:
                break
            ne = ne.next
        
        head.next = self.reverseKGroup(cur, k)
        return prev
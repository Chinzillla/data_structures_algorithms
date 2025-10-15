class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def has_cycle(nodes: Node) -> bool:
        slow = nodes
        fast = nodes.next.next

        while fast and fast.next:
            if fast.val == slow.val:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def has_cycle(nodes: Node) -> bool:
        slow = nodes
        fast = nodes

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        
        return False
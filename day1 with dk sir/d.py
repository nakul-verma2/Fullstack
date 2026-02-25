from typing import Optional, List

# 1. Definition for a singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: If the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first = head
        second = head.next
        
        # Recursive Step: 
        # first.next will point to the result of the swap on the rest of the list
        first.next = self.swapPairs(second.next)
        
        # Swapping: second points back to first
        second.next = first
        
        # Now 'second' is the new head of this pair
        return second

# --- HELPER UTILITIES TO RUN IN VS CODE ---

def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Converts a Python list into a Linked List."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head: Optional[ListNode]):
    """Prints the linked list in a readable format."""
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements) if elements else "Empty List")

# --- TEST EXECUTION ---

if __name__ == "__main__":
    # Input numbers
    nums = [1, 2, 3, 4, 5]
    print(f"Original List: {nums}")
    
    # Convert to Linked List
    head = create_linked_list(nums)
    
    # Run the Solution
    sol = Solution()
    swapped_head = sol.swapPairs(head)
    
    # Output the result
    print("Swapped List:  ", end="")
    print_linked_list(swapped_head)
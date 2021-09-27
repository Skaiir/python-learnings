class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):        
    if head and head.next:
        stack = []
        while head.next:
            stack.append(head)
            head = head.next
        head.next = stack[-1]
        while stack:
            
            pop = stack.pop()
            pop.next = stack[-1] if stack else None

            stack.pop().next = stack[-1] if stack else None


            
    return head


head = ListNode(1, ListNode(2, ListNode(3)))

worker = head
while worker:
    print(worker.val)
    worker = worker.next

head = reverseList(head)

worker = head
while worker:
    print(worker.val)
    worker = worker.next
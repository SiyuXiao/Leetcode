class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

a = [1, 1, 2, 3, 3]
p = head = ListNode(a[0])
for b in a[1:]:
	p.next = ListNode(b)
	p = p.next

def deleteDuplicates(head):
    if head == None:
        return None
    first = head
    second = head.next
    while second:
        if first.val == second.val:
            second = second.next
            first.next = second
        else:
            first = second
            second = second.next
    return head
deleteDuplicates(head)

#王警剑写的
def deleteDuplicates(head):
    if head is None:
        return head
    else:
        temp = head
        head = head.next
        temp.next = None
        p = new_head = temp
        while head is not None:
            if head.val > p.val:
                temp = head
                head = head.next
                temp.next = None
                p.next = temp
                p = p.next
            else:
                head = head.next
    return new_head
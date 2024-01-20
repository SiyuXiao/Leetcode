class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#我最开始转换成列表做
'''
def reverseList(head):
    if head == None:
        return None
    a = []
    while head:
        a.insert(0, head.val)
        head = head.next
    newhead = ListNode(a[0])
    p = newhead
    for b in a[1:]:
        p.next = ListNode(b)
        p = p.next
    return newhead
'''

#后来我又用链表做出来了，用的迭代的思想
def reverseList(head):
    p = head
    newhead = None
    while p:
        if newhead is None:
            newhead = p
            p = p.next
            newhead.next = None
        else:
            temp = p
            p = p.next
            temp.next = newhead
            newhead = temp
    return newhead

#答案的算法，篇幅比我少点，但解决思想一样，也是迭代
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

#这是我最开始写的，跑死了
'''
def mergeTwoLists(l1, l2):
    p = ListNode(-1)
    head = l1
    while l1 and l2:
        p.next = l1     #l1赋值给p.next
        p.next.next = l2#相当于l1.next = l2
        l1 = l1.next    #问题就出在这步，l1.next现在是l2，这步l1更新本来应该是l1这个链表下一个节点的，结果更新成l2头节点了
        l2 = l2.next
        p = p.next.next
    return head
result = mergeTwoLists(l1, l2)
print(result)
'''
#我在原有基础上又改改，但是出来结果不对
'''
def mergeTwoLists(l1, l2):
    p = ListNode(-1)
    head = l1
    while l1 and l2:
        p.next = l1
        p = p.next
        print(p.val)
        p.next = l2#p现在是l1，p.next = l2相当于l1.next = l2，导致原来l1后面的节点全没了，这是我错误的原因，和上一个程序错的本质原因一样
        p = p.next
        l1 = l1.next
        l2 = l2.next
        print(p.val)
    return head
result = mergeTwoLists(l1, l2)
#print(result.val)
'''
#上一个程序把l1 = l1.next换一个位置就对了，当然也仅适用于这一个测试样例罢了
'''
def mergeTwoLists(l1, l2):
    p = ListNode(-1)
    head = l1
    while l1 and l2:
        p.next = l1
        p = p.next
        l1 = l1.next#让l1及时地变成l1.next
        print(p.val)
        p.next = l2
        p = p.next
        l2 = l2.next
        print(p.val)
    return head
result = mergeTwoLists(l1, l2)
#print(result.val)
'''

#这是王警剑写的
'''
def mergeTwoLists(l1, l2):
    head = None
    while True:
        if l1 is None and l2 is None:
            break
        elif l1 is None and l2 is not None:
            if head is None:
                head = l2
            else:
                p.next = l2
            break
        elif l1 is not None and l2 is None:
            if head is None:
                head = l1
            else:
                p.next = l1
            break
        else:
            if l1.val <= l2.val:
                if head is None:
                    p = head = l1
                else:
                    p.next = l1
                    p = p.next
                l1 = l1.next
            else:
                if head is None:
                    p = head = l2
                else:
                    p.next = l2
                    p = p.next
                l2 = l2.next
    return head
result = mergeTwoLists(l1, l2)
print(result.val)
'''

#我自己写的
'''
def mergeTwoLists(l1, l2):
    head = None
    p = None
    if l1 is None and l2 is None:
        return None
    while l1 and l2:
        if l1.val <= l2.val:
            temp1 = l1
            l1 = l1.next
            temp1.next = None
            if head is None:
                p = head = temp1
            else:
                p.next = temp1
                p = p.next
        else:
            temp2 = l2
            l2 = l2.next
            temp2.next = None
            if head is None:
                p = head = temp2
            else:
                p.next = temp2
                p = p.next
    if l1 is None and l2 is not None:
        if p is None:
            return l2
        else:
            p.next = l2
    if l1 is not None and l2 is None:
        if p is None:
            return l1
        else:
            p.next = l1
        p.next = l1
    return head
result = mergeTwoLists(l1, l2)
print(result.val)
'''
#答案给的方法好巧妙啊，巧妙地解决了中点问题
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#我自己写的解法
def middleNode(self, head):
    p = head
    cnt1 = cnt = 0
    while p:
        cnt +=1
        p = p.next
    while cnt1 < cnt//2:
        cnt1 += 1
        head = head.next
    return head
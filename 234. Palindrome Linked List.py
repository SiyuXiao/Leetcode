#我最开始的想法是把原链表倒序，然后把倒序的链表和原链表比较
#倒序的过程中破坏了原链表，所以这就涉及到了链表复制的问题，所以我先尝试复制链表
'''
#创建一个链表
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
a = [1, 2, 3, 4, 5]
head = p = ListNode(a[0])
for b in a[1:]:
	p.next = ListNode(b)
	p = p.next
#复制创建的链表
head1 = pp = ListNode(head.val)
while head.next:
	head = head.next
	pp.next = ListNode(head.val)
	pp = pp.next
#把复制的链表打印出来
while head1:
	print(head1.val)
	head1 = head1.next
'''
#知道了如何复制链表后，接下来实现我的算法
#但是这种方法空间复杂度是n
def isPalindrome(self, head):
    if head is None:
        return True
    a = None
    p = head1 = ListNode(head.val)
    while head:
        b = head
        head = head.next
        b.next = a
        a = b
        if head:
            p.next = ListNode(head.val)
            p = p.next
    while a:
        if a.val == head1.val:
            a = a.next
            head1 = head1.next
        else:
            return False
    return True

#我必须得提一下我在这个过程中走过的坑：
#b.next = a，这时候b.next在等号左边，
#是被赋值的东西，也就是原有b和head同时指向的内存的.next被改变了
#第一轮循环b.next = a，即首节点p.next = None，
#而第二轮循环中b等于新的head，这时候b和第一个节点就没关系了，
#所以p.next就一直是None了，所以return p时p.val = a, p.next = None
def isPalindrome(self, head):
    a = None
    p = head
    while head:
        b = head
        head = head.next
        b.next = a
        a = b
    return p
    while a:
        if a.val == head1.val:
            a = a.next
            head1 = head1.next
        else:
            return head1
    return True

#最后的解法，其实判断一组数是否是回文数，有一个最佳算法：
#先判断数组中数的个数是奇数还是偶数
#奇数的话第一个和最后一个比，第二个和倒数第二个比。。。中间的一个数不用管
#偶数的话也是这么比，只不过没有中间数了
#这个题我把原链表截成了前后两半，满足了时间复杂度为n,空间复杂度为1的条件，击败了100%的对手，虽然这个跟网速有关，不是很准
def isPalindrome(self, head):
    if head is None or head.next is None:
        return True
    a = None
    p1 = p = head
    cnt = 0
    cnt1 = 1
    while p:
        cnt += 1
        p = p.next
    while cnt1 < cnt // 2:
        cnt1 += 1
        p1 = p1.next
    if cnt % 2 == 0:
        p2 = p1.next
        p1.next = None
    else:
        p2 = p1.next.next
        p1.next = None  #p2是后半个链表的首节点，head是前半个链表的首节点
    while head:
        b = head
        head = head.next
        b.next = a
        a = b
    while a:
        if a.val == p2.val:
            a = a.next
            p2 = p2.next
        else:
            return False
    return True


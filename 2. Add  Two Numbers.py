#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# In[2]:


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1temp = l1
        l2temp = l2
        
        temp1 = 0
        temp2 = 0
        
        i = 0
        while (l1temp != None):
            if l1temp.val != None:
                temp1 = temp1 + l1temp.val * (10 ** i)
            l1temp = l1temp.next
            i = i + 1
        i = 0
        while (l2temp != None):
            if l2temp.val != None:
                temp2 = temp2 + l2temp.val * (10 ** i)
            l2temp = l2temp.next
            i = i + 1

        sum = temp1 + temp2
        result = []
        i = 0
        while (sum > 0):
            result.append(ListNode(sum % 10))
            if i >= 1:
                result[i - 1].next = result[i]
            sum = sum // 10
            i = i + 1
        return result[0]


# In[3]:


n1=ListNode(1)


# In[4]:


n2=ListNode(2)


# In[5]:


n3=ListNode(3)


# In[6]:


n1.next=n2


# In[7]:


n2.next=n3


# In[8]:


nn1=ListNode(4)


# In[10]:


nn2=ListNode(5)


# In[12]:


nn3=ListNode(6)


# In[13]:


nn1.next=nn2


# In[14]:


nn2.next=nn3


# In[15]:


Solution().addTwoNumbers(n1,nn1).val


# In[16]:


Solution().addTwoNumbers(n1,nn1).next.val


# In[17]:


Solution().addTwoNumbers(n1,nn1).next.next.val


# In[ ]:
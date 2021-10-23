# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l=[]
        for i in lists:
            temp=i
            if i!=None:
                while(temp):
                    l.append(temp.val)
                    temp=temp.next
        l.sort()
        if len(l)==0:
            return None
        else:
            root=ListNode(l[0])
            temp=root
            for i in range(1,len(l)):
                x=ListNode(l[i])
                temp.next=x
                temp=x
        return root

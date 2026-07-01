# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev=head
        temp=prev.next
        count=1
        critical=[]
        while temp.next:
            if temp.val>prev.val and temp.val>temp.next.val:
                critical.append(count)
            elif temp.val<prev.val and temp.val<temp.next.val:
                critical.append(count)
            prev=temp 
            temp=temp.next
            
            count+=1

        if len(critical)<2:
            return [-1,-1]

        mini=float("inf")
        for i in range(1,len(critical)):
            mini=min(mini,(critical[i]-critical[i-1]))
        maxm=critical[-1]-critical[0]
        return [mini,maxm]        


        
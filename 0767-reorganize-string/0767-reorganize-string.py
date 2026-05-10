class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        from collections import Counter 

        freq=Counter(s)
        max_heap=[]
        for ch,count in freq.items():
            heapq.heappush(max_heap,(-count,ch))


        res=[]
        prev_count=0
        prev_ch=""

        while max_heap:
            count,ch=heapq.heappop(max_heap)
            res.append(ch) 

            if prev_count<0:
                heapq.heappush(max_heap,(prev_count,prev_ch))

            count+=1
            prev_count=count
            prev_ch=ch

        ans="".join(res)
        if len(ans)!=len(s):
            return ""
        return ans    

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq={}
        for i,ch in enumerate(s):
            freq[ch]=i

        visited=set()
        stack=[]

        for i in range(len(s)):
            ch=s[i]
            if ch in visited:
                continue


            while stack and stack[-1]>ch and freq[stack[-1]]>i:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)


        return "".join(stack)                
            
        
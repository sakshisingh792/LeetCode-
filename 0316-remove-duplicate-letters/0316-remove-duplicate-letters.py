class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last={}
        for i in range(len(s)):
            ch=s[i]
            last[ch]=i

        taken=set()
        stack=[]
        for i in range(len(s)):
            ch=s[i]

            if ch in taken:
                continue

            while stack and stack[-1]>ch and last[stack[-1]]>i:
                taken.remove(stack.pop())

            stack.append(ch)
            taken.add(ch)
        return "".join(stack)                

        
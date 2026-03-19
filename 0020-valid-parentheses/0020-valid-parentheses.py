class Solution:
    def isValid(self, s: str) -> bool:
      dict={")":"(","}":"{","]":"["}
      stack=[]
      for ch in s:
        if ch in dict.values():
            stack.append(ch)
        elif   ch in dict:
            if not stack or stack[-1]!=dict[ch]:
                return False
            stack.pop()
        else:
            return False


      return not stack          


                         




        
        
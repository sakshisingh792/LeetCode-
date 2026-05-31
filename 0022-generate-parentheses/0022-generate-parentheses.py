class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openn=n
        close=n
        out=""
        ans=[]
        def parenthesis(openn,close,out):
            if openn==0 and close==0:
                ans.append(out)
                return 
            if openn!=0:
                out2=out
                out2+="("
                parenthesis(openn-1,close,out2)

            if close> openn:
                out2=out
                out2+=")"
                parenthesis(openn,close-1,out2) 
        parenthesis(n, n, "")

        return ans        



        
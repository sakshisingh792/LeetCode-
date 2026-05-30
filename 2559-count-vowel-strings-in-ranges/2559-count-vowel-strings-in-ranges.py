class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel="aeiou"
        prefix=[0]*len(words)
        count=0
        for i in range(len(words)):
                word=words[i]
                lenn=len(word)
                if word[0] in vowel and word[lenn-1] in vowel:
                    count+=1
                prefix[i]=count
        ans=[]
        for l , r in queries:
            if l==0 :
                ans.append(prefix[r])
    
            else:
                ans.append(prefix[r]-prefix[l-1])
        return ans        
                        

                
          
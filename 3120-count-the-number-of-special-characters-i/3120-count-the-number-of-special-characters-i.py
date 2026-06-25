class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash={}
        ans=set()
        for i in range(len(word)):
            ch=word[i]
            if ch!=ch.upper() and ch.upper() in hash:
                ans.add(ch.lower())
            elif ch!=ch.lower() and ch.lower() in hash:
                ans.add(ch.lower())

            hash[word[i]]=hash.get(word[i],0)+1

        return len(ans)            
        
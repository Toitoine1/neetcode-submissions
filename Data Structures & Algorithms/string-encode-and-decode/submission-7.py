class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs :
            encoded = encoded + str(len(s)) + ':'
        encoded =encoded + ';'
        for s in strs :
            encoded = encoded + s
        return encoded

    def lenstr2lenlist (self, string : str) -> List[int] :
        l=[]
        pointer = -1
        char = ''
        curnum = ''
        while char != ';' :
            if char == ':' :
                l.append(int(curnum))
                curnum = ''
            else :
                curnum = curnum + char
            pointer = pointer + 1
            char = string[pointer] 
        return l
        


    def decode(self, s: str) -> List[str]:
        l = self.lenstr2lenlist(s)
        i = -1 
        c = ''
        while c != ';' : 
            i+=1
            c = s[i]
        i=i+1
        words = []
        for lenw in l : 
            words.append(s[i:i+lenw])
            i+=lenw
        return words
            

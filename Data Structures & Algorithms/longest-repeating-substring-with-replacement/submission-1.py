class Solution:
    def oneletter(self, s, k, char : str) :
        memoryk = k
        mx = 1
        down = 0
        up = 0
        n = len(s) -1
        if s[0] != char :
            k+=-1
        while up != n :
            #print(down, s[down], up, s[up],k, mx)
            if k >= 0  :
                mx = max(mx,up-down+1)
                up +=1
                if s[up] != char :
                    k+=-1
            else :
                down+=1
                if s[down-1] != char :
                    k+=1
        if k >= 0  :
            mx = max(mx,up-down+1)
        k = memoryk
        return mx 

    def characterReplacement(self, s: str, k: int) -> int:
        mx = 0
        alphabet = set(s)
        for char in alphabet :
            #print(char,self.oneletter(s,k,char))
            mx = max(mx,self.oneletter(s,k,char))
        return mx 

        
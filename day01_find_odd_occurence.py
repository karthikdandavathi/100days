class Solution:
    def main(self,inp):
        if not inp:
            return
        
        out = {}
        for each_elm in inp:
            if each_elm in out:
                out[each_elm] = out[each_elm] + 1
            else:
                out[each_elm] = 1

        for k,v in out.items():
            if v%2!=0:
                return k

        return





if __name__ == '__main__':
    inp = [3,2,4,4,2,1,1]
    sol = Solution()
    print(sol.main(inp))
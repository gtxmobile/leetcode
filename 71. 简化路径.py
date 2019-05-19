class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        res=[]
        tmp=path.split('/');
        for s in tmp:
            if s and s is not '.':
                if s=='..':
                    if res:
                        res.pop()
                else:
                    res.append(s)
        if not res:
            return '/'
        else:
            return '/'+'/'.join(res)
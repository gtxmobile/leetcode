#coding: utf8
#ceng bianli
class Solution:
    def connect(self,root):
        ceng=[]
        if root==None:
            return
        ceng.append(root)
        while 1:
            for i in range(len(ceng[:-1])):
                ceng[i].next=ceng[i+1]
            ceng[-1].next=None
            tmp=[]
            for n in ceng:
                if n.left==None:
                    return root
                tmp.extend([n.left,n.right])
            ceng=tmp





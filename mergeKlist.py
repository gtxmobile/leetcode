
import heapq
def mergeKLists(lists):
        root=ListNode(-1)
        cur=root
        dlen=len(lists)
        tail=-1
        while dlen:
                MIN=99999
                i=0
                tmp=-1
                while i<dlen:
                    if not lists[i]:
                        lists[i],lists[tail]=lists[tail],lists[i]
                        tail-=1
                        dlen-=1
                        continue
                    if lists[i].val<MIN:
                        tmp=i
                        MIN=lists[i].val
                    i+=1
                if tmp>-1:
                    #print lists[tmp].val,
                    cur.next=ListNode(lists[tmp].val)
                    cur=cur.next
                    lists[tmp]=lists[tmp].next

        return root.next


def mergeKLists2(lists):
        root=ListNode(-1)
        cur=root
        small=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(small,(lists[i].val,i))
        while small:
                _,i=heapq.heappop(small)
                cur.next=lists[i]
                cur=cur.next
                lists[i]=lists[i].next
                if lists[i]:
                    heapq.heappush(small,(lists[i].val,i))
        return root.next

def partition(head, x):
        zuo=ListNode(-1)
        you=ListNode(-1)
        zroot=zuo
        yroot=you
        cur=head
        while cur:
            if cur.val<x:
                zuo.next=cur
                zuo=cur
            else:
                you.next=cur
                you=cur
            cur=cur.next
        you.next=None
        zuo.next=yroot.next
        return zroot.next

def deleteDuplicates(head):
        if not head:
            return None
        prv=ListNode(-1)
        prv.next=head
        cur=head
        head=prv
        while cur:
            while cur.val==tmp:
                cur=cur.next
                prv.next=None
            else:
                tmp=cur.val
                if prv.next:
                    prv=prv.next
                prv.next=cur
                cur=cur.next
                prv=prv.next
        return head.next

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def tomid(self,head,tail):
        if head==tail:
            return
        mid=head
        kuai=head
        if kuai!=tail and kuai.next!=tail:
            mid=mid.next
            kuai=kuai.next.next
        root=TreeNode(mid.val)
        root.left=self.tomid(head,mid)
        root.right=self.tomid(mid.next,tail)
        return root

    def sortedListToBST(self, head):
        return self.tomid(head,None)

def printTree(root):
    if not root:return
    print root.val
    printTree(root.left)
    printTree(root.right)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from random import randint
lists=[]

def genalist(sorted=False):
    root=ListNode(randint(1,10))
    cur=root
    for j in range(randint(20000,20000)):
        val=(cur.val+randint(0,10) if sorted else randint(1,10))
        cur.next=ListNode(val)
        cur=cur.next
    return root

def genKlist(k):
    for i in range(k):
       lists.append(genalist(True))

def printlist(l):
    while l:
        print l.val,
        l=l.next
    print
def kprintl(lists):
    for l in lists:
        printlist(l)

inlist=genalist(True)
printlist(inlist)
#printlist(partition(inlist,5))
#printlist(deleteDuplicates(inlist))
printTree(Solution().sortedListToBST(inlist))
#
genKlist(randint(1,10))
#kprintl(lists)
print
#printlist(mergeKLists2(lists))
def mergek(lists):
    head = ListNode(99999);
    for i in range(len(lists)):
        p1 = head.next;
        p2 = lists[i];
        pre = head;
        while p1!= None and p2!= None:
            if(p1.val >= p2.val):
                pre.next = p2;
                p2 = p2.next; pre = pre.next;
                pre.next = p1;
                continue;
            pre = p1;
            p1 = p1.next;
        if(p2 != None):
            pre.next = p2;
    return head.next;

#printlist(mergek(lists))
import heapq

a=[randint(1,10) for i in range(10)]
ret=[]
#print a
for i in range(len(a)):
    heapq.heappush(ret,(a[i],i))
for i in a:
    #print heapq.heappop(ret)
    pass
#print ret



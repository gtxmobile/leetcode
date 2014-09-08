def isPalindrome(x):
        cnt=1
        x=abs(x)
        while x/cnt>=10:
            print 1
            cnt*=10
        while x>0:
            if x%10!=x/cnt:
                print 1
                return False
            x=x%cnt/10
            cnt/=100
        return True

print isPalindrome(2147483647)

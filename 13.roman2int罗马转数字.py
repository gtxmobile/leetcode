#coding:utf-8
def romanToInt(self, string):
    table={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    returnint=0
    continueyes=True
    while string:
        if len(string)>=2:
            if table.get(string[0:2]):
                returnint+=table.get(string[0:2])
                string=string[2:]
                continue
        returnint+=table.get(string[0:1])
        string=string[1:]
    return returnint

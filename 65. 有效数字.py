class Solution65:
    def isNumber(self, s: str) -> bool:
        is_num = False
        is_dot = False
        is_e = False
        ss = s.strip()
        l = len(ss)-1
        for i, c in enumerate(ss):
            if c.isdigit():
                is_num = True
            elif c == ".":
                if is_dot or (not is_num and i ==l) or is_e:
                    return False
                is_dot = True
            elif c in ("e","E"):
                if is_e or i==l or not is_num:
                    return False
                is_e =  True
            elif c in ("+","-"):
                if (i>0 and ss[i-1] not in ("e","E")) or i==l:
                    return False
            else:
                return False
        return True
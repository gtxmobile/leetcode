class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        llen = -1
        ret = []
        line = []
        for w in words:
            llen += len(w)
            if llen < maxWidth:
                llen += 1
                line.append(w)
            else:
                llen -= len(w)
                wcount = len(line)
                spacelen = maxWidth - llen+wcount-1
                if wcount > 1:
                    single = spacelen / (wcount-1)
                    left = spacelen % (wcount-1)
                else:
                    left = spacelen
                    line[0]+=" "*left
                ss = [line[0]]
                for l in line[1:]:
                    ss.append(" " * single)

                    if left:
                        ss.append(" ")
                        left -= 1
                    ss.append(l)
                ret.append("".join(ss))
                line = [w]
                llen = len(w)

        if line:
            ret.append(" ".join(line))
        if ret:
            line = ret[-1]
            newline = ""
            for i in line.split(" "):
                if i:
                    newline += i
                    maxWidth = maxWidth - len(i) - 1
                    if maxWidth >= 0:
                        newline += " "
            for i in range(maxWidth):
                newline += " "
            ret[-1] = newline
        return ret
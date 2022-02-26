class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        try:
            while 1:
                A.remove(elem)
        except:
            return len(A)

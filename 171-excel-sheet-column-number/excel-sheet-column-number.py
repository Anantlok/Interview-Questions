class Solution(object):
    def titleToNumber(self, columnTitle):
        result=0
        for ch in columnTitle:
            result= result*26+(ord(ch)-64)
        return result
        
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while columnNumber > 0:
            columnNumber -= 1
            letter = chr(ord('A') + columnNumber % 26)
            answer = letter + answer
            columnNumber //= 26
        return answer
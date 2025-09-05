class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        new_num, cnt = num1, 1
        while True:
            new_num -= num2
            if new_num < cnt:
                return -1
            if cnt >= new_num.bit_count():
                return cnt
            cnt += 1
        return -1

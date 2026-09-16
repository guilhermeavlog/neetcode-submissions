class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if digits[i] == 9 and i == len(digits)-1:
                digits.append(1)
                digits[i] = 0
                one -= 1
            elif digits[i] == 9:
                digits[i] = 0
                i += 1
            else:
                digits[i] += 1
                one -= 1

        return digits[::-1]
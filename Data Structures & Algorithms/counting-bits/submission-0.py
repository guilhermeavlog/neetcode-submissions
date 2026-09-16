class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = [0] * (n+1)

        for num in range(n+1):
            bin_num = bin(num)
            count = 0

            for c in bin_num:
                if c == '1':
                    count += 1

            sol[num] = count

        return sol



        
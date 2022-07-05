class Solution:
    def checkRecord(self, n: int) -> int:
        """
        award
        absent < 2 days
        late < 3 consecutive days
        """
        memo = {}

        def recurse(n, num_absents, num_consecutive_late):
            nonlocal memo

            if n == 0:
                return 1

            if (n, num_absents, num_consecutive_late) in memo:
                return memo[(n, num_absents, num_consecutive_late)]

            tot_poss = 0

            if num_absents == 1:

                if num_consecutive_late == 2:
                    tot_poss += recurse(n - 1, num_absents, 0)

                else:
                    tot_poss += recurse(n - 1, num_absents, num_consecutive_late + 1)
                    tot_poss += recurse(n - 1, num_absents, 0)

            else:

                if num_consecutive_late == 2:
                    tot_poss += recurse(n - 1, num_absents, 0)
                    tot_poss += recurse(n - 1, num_absents + 1, 0)

                else:
                    tot_poss += recurse(n - 1, num_absents, num_consecutive_late + 1)
                    tot_poss += recurse(n - 1, num_absents + 1, 0)
                    tot_poss += recurse(n - 1, num_absents, 0)

            memo[(n, num_absents, num_consecutive_late)] = tot_poss

            return memo[(n, num_absents, num_consecutive_late)]

        return recurse(n, 0, 0) % (10 ** 9 + 7)

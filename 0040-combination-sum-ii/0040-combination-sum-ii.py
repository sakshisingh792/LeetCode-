class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        candidates.sort()
        res = []

        def solve(i, rem, ds):

            if rem == 0:
                res.append(ds[:])
                return

            if i == len(candidates):
                return

            if candidates[i] > rem:
                return

            # TAKE
            ds.append(candidates[i])

            # move to next index
            solve(i + 1, rem - candidates[i], ds)

            ds.pop()

            # SKIP duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # NOT TAKE
            solve(i + 1, rem, ds)

        solve(0, target, [])
        return res
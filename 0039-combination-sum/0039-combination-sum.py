class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[]
        candidates.sort()
        def dfs(target, path, i):
            if target== 0:
                dp.append(path[:])
                return
            if target<0:
                return
            for j in range(i, len(candidates)):
                if candidates[j] > target:
                    break
                path.append(candidates[j])
                dfs(target - candidates[j], path, j)
                path.pop()
        dfs(target, [], 0)
        return dp

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort()
        max_f = count[-1]
        count_task = 0
        for task in count:
            if task == max_f:
                count_task += 1
        return max(len(tasks), (max_f - 1) * (n + 1) + count_task )
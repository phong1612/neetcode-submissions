class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [] #Stack to track not closed day
        day_wait = [0] * n
        index_track = []
        current_ind = 0
        for i in range(n):
            if res == []:
                res.append(temperatures[i])
                index_track.append(i)
                continue
            while res != []:
                if temperatures[i] > res[-1]:
                    day_wait[index_track[-1]] = i - index_track[-1]
                    res.pop()
                    index_track.pop()
                else:
                    break
            res.append(temperatures[i])
            index_track.append(i)
        return day_wait
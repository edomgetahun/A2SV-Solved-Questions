class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        rabbits = Counter(answers)
        for ans in answers:
            if ans in rabbits:
                total += ans + 1
                group_size = ans + 1
                rabbits[ans] -= min(rabbits[ans], group_size)
                if rabbits[ans] <= 0:
                    del rabbits[ans]
        return total
            



        
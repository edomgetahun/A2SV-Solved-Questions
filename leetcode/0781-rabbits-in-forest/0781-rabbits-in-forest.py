class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        rabbits = Counter(answers)
        for ans in answers:
            if ans in rabbits:
                group_size = ans + 1
                total += group_size
                if rabbits[ans] >= group_size:
                    rabbits[ans] -= group_size
                else:
                    rabbits[ans] = 0
                if rabbits[ans] <= 0:
                    del rabbits[ans]
        return total
            



        
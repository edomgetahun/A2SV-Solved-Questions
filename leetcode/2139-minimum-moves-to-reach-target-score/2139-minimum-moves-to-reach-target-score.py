class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        if maxDoubles == 0:
            move = target - 1  
            return move
        
        while target > 1:
            if target % 2 == 1:
                target -= 1
                move += 1
            else:
                if maxDoubles > 0:
                    target = target // 2
                    move += 1
                    maxDoubles -= 1
                else:
                    break
        move += target - 1
        return move



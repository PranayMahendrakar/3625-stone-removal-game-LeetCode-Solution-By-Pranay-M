class Solution:
    def canAliceWin(self, n: int) -> bool:
        # Alice removes 10, Bob removes 9, Alice removes 8, etc.
        stones_to_remove = 10
        alice_turn = True
        
        while n >= stones_to_remove and stones_to_remove > 0:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn
        
        # If it's Bob's turn and he can't move, Alice wins
        return not alice_turn
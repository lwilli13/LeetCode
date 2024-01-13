class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        elif money < 8:
            return 0
        
        money -= children

        rec = money//7
        rem = money%7
        
        if rem == 3 and rec == children - 1:
                return children - 2
        if rem == 0 and rec == children:
            return rec

        return min (rec, children-1)
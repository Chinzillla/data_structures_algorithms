class Solution:
    def pivotInteger(self, n: int) -> int:
        
        total = n * (n + 1) // 2
        for i in range (1, n + 1):
            print(i)
            
            # sum of all natrual numbers to n = n(n + 1)//2
            left = i * (i + 1) // 2
            
            # sum of all natural numbers from x-1 to n is total - sum(1..x-1)
            # total - (x - 1 + 1)(x - 1)//2 = total - x(x - 1) // 2
            right = total - (i - 1) * i // 2

            if left == right:
                return i
                
        return -1
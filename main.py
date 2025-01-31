from cmath import sqrt

class Calculations:
    def __init__(self):
        self.n = 1
        self.results = {}
    
    def G(self, n):
        total = 0
        numbers = list(range(1, n+1))
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)+1):
                sub = numbers[i:j]
                for idx, num in enumerate(sub):
                    if (idx + 1) % 3 == 0:  # 1-based 3rd position
                        total -= num
                    else:
                        total += num
        return total
        
    def equation(self, n):
        """
        (G(3n) - 2G(3n-1) + G(3n-2))/3
        """
        return (self.G(3*n) - 2*self.G(3*n-1) + self.G(3*n-2))/3

calculation = Calculations()

consecutive_count = 0
prev_sqrt = None

for i in range(1, 400, 1):
    result = calculation.equation(i)
    sq = sqrt(result)
    
    if sq.imag == 0 and sq.real > 0 and sq.real.is_integer():
        current_sqrt = int(sq.real)
        if prev_sqrt is not None and current_sqrt == prev_sqrt + 1:
            consecutive_count += 1
            print(f"Found consecutive square root: {current_sqrt} at input {i}")
        else:
            consecutive_count = 1
        prev_sqrt = current_sqrt
        calculation.results[i] = 0
    else:
        prev_sqrt = None
        consecutive_count = 0
        calculation.results[i] = 1
        
    if consecutive_count >= 3:
        print(f"Found {consecutive_count} consecutive square roots ending at input {i}")

non_perfect_square = sum(calculation.result)
perfect_squares = len(calculation.result) - non_perfect_square

print(f"Perfect squares: {perfect_squares} \nNon-perfect squares: {non_perfect_square}")

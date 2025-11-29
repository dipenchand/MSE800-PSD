class MathSeries:
    # @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)



    # @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2))
    
    def fibonacci_sequence(self, n):
        if n <= 0:
            return []
        elif n == 1:    
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            seq = self.fibonacci_sequence(n - 1)
            seq.append(seq[-1] + seq[-2])
            return seq
        
class RunMathSeries:
    def run():
        n = int(input("Enter a non-negative integer: "))
        math_series = MathSeries()
        
        print("Fibonacci Series:", math_series.fibonacci_sequence(n))

if __name__ == "__main__":
    RunMathSeries.run()

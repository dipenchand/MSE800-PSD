class MathSeries:
    def __init__(self, n):
        self.n = n

    def test(self):
        print(self.n * 4)

    def factorial_recursive(self):
        return self._factorial(self.n)

    def _factorial(self, num):
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if num in (0, 1):
            return 1
        return num * self._factorial(num - 1)

    def fibonacci_recursive(self):
        if self.n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if self.n == 0:
            return 0
        if self.n == 1:
            return 1
        return (self.fibonacci_recursive(self.n - 1) +
                self.fibonacci_recursive(self.n - 2))

    # New method to print all Fibonacci values up to n
    def fibonacci_series(self):
        series = []
        for i in range(self.n + 1):
            series.append(self.fibonacci_recursive(i))
        return series


if __name__ == "__main__":
    n = 5

    # Create an object
    obj1 = MathSeries(n)

    # Call using the object (works because no self is expected)
    print("Factorial (recursive):", obj1.factorial_recursive())
    # print("Fibonacci (recursive):", obj1.fibonacci_recursive(obj1.n))

    # # Print the entire Fibonacci series
    # print(f"Fibonacci series (0 to {obj1.n}):", obj1.fibonacci_series(obj1.n))

    # obj1.test()
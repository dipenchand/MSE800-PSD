class RecursiveMath:
    def factorial(n):
        if n == 0:
            return 1
        return n * RecursiveMath.factorial(n - 1)

    def fibonacci(n):
        if n <= 1:
            return n
        return RecursiveMath.fibonacci(n - 1) + RecursiveMath.fibonacci(n - 2)


class Calculator:
    result = None

    recursive_math = RecursiveMath()
    
    def display_menu():
        print("Choose an operation:")
        print("1. Factorial")
        print("2. Fibonacci")
        print()
    
    def run():
        Calculator.display_menu()
        choice = input("Enter choice (1/2): ")
        
        if choice == "1":
            n = int(input("Enter a non-negative integer: "))
            ans = Calculator.recursive_math.factorial(n)
        elif choice == "2":
            n = int(input("Enter a non-negative integer: "))
            ans = Calculator.recursive_math.fibonacci(n)
        else:
            ans = "Invalid choice"
        
        print(f"\nFinal result: {ans}")


def main():
    Calculator.run()


if __name__ == "__main__":
    main()
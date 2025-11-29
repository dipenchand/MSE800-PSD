class RecursiveMath:
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


class Calculator:
    result = None

    recursive_math = RecursiveMath()
    
    def display_menu():
        print("Choose an operation:")
        print("1. Factorial")
        print("2. Fibonacci")
        print()
    
    def get_user_input():
        choice = input("Enter choice (1/2): ")
        return choice
    
    def run():
        display_menu()
        choice = get_user_input()
        
        if choice == "1":
            n = int(input("Enter a non-negative integer: "))
            ans = recursive_math.factorial(n)
        elif choice == "2":
            n = int(input("Enter a non-negative integer: "))
            ans = recursive_math.fibonacci(n)
        else:
            ans = "Invalid choice"
        
        print(f"\nFinal result: {ans}")


def main():
    Calculator.run()


if __name__ == "__main__":
    main()
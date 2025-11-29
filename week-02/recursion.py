def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print("Choose an operation:")
    print("1. Factorial")
    print("2. Fibonacci")
    print()

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        n = int(input("Enter a non-negative integer: "))
        ans = factorial(n)
    elif choice == "2":
        n = int(input("Enter a non-negative integer: "))
        ans = fibonacci(n)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)

if __name__ == "__main__":
    main()
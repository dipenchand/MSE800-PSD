def fibonacci(n):
    a,b = 0,1
    result = []
    
    for _ in range(n):
        result.append(a)
        a,b = b, a+b
        
    return result

def main():
    n = int(input("Enter number to generated Fibonacci Series:"))
    result = fibonacci(n)
    print("Fibonacci series:", result)


if __name__ == "__main__":
    main()
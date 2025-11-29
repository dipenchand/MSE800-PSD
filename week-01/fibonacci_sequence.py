# import fibonacci

def fibonacciLoop(n):
    a,b = 0,1
    result = []
    
    for _ in range(n):
        result.append(a)
        a,b = b, a+b
        
    return result

def fibonacciRecursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacciRecursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def fibonacciRec(n):
    if n <= 1:
        return n
    else:
        return fibonacciRec(n-1) + fibonacciRec(n-2)

def main():
    n = int(input("Enter the number of Fibonacci terms to generate: "))
    
    # Using manual for loop
    print("Using manual for loop:", fibonacciLoop(n))
    
    # Using Recursion
    print("Using Recursion:", fibonacciRecursive(n))
    
    print("Using Recursion by Teacher:", fibonacciRec(n))
    
    # Using Package (demonstrating function call)
    # print("Using Package:", fibonacci.fibo(n))


if __name__ == "__main__":
    main()
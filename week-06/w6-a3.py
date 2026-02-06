# f = lambda x, y: x * y
# print(f(5, 2))

# # Factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))

# # Factorial with lambda
# fact = lambda n: 1 if n == 0 else n * fact(n - 1)
# print(fact(5))


# data = []
# for i in range(5):
#     data.append(lambda a, i=i*2: i*a)

# for d in data:
#     print(d(5))

# data[0](10)





data = ['a5', 'a2', 'b1', 'b3', 'c2']
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
print(sorted_data)

# temp = lambda x: (x[0], int(x[1:]))
# print(temp('a512'))
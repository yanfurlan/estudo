def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Teste
print(factorial(5))  # 120
print(factorial(0))  # 1

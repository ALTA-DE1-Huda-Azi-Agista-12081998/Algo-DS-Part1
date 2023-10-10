def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, number + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144
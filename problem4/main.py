def generate_primes_grid(width, height, start):
    result = ""

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    current_num = start
    for _ in range(height):
        row = " ".join(str(num) for num in range(current_num, current_num + width) if is_prime(num))
        result += f"{row}\n"
        current_num = current_num + width

    return result.strip()

# Test cases
print(generate_primes_grid(2, 3, 13))
# 17 19
# 23 29
# 31 37

print(generate_primes_grid(5, 2, 1))
# 2 3 5 7 11
# 13 17 19 23 29

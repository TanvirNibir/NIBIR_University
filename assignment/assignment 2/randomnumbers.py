import random

code_3_digit = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]

code_4_digit = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

print("3-digit combination lock code:", ''.join(str(digit) for digit in code_3_digit))
print("4-digit combination lock code:", ''.join(str(digit) for digit in code_4_digit))

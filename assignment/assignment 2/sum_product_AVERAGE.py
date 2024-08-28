def sum_product_AVERAGE(n1, n2, m3):
    total_sum = n1 + n2 + m3
    product = n1 * n2 * m3
    average = (n1 + n2 + m3) / 3
    return total_sum, product, average

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
total_sum, product, average = sum_product_AVERAGE(n1, n2, n3)
print(f"total_sum {total_sum}")
print(f"product {product}")
print(f"average {average}")




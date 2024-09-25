import random

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside_circle += 1
    return 4 * inside_circle / num_points

num_points = int(input("Enter the number of random points to generate: "))
approx_pi = estimate_pi(num_points)
print(f"Approximation of π: {approx_pi}")

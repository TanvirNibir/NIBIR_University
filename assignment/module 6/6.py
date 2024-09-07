import math


def unit_price(d, p):
    return p / (math.pi * (d / 2) ** 2 / 1_000_000)


def main():
    d1, p1 = map(float, input("Pizza 1 (diameter price): ").split())
    d2, p2 = map(float, input("Pizza 2 (diameter price): ").split())

    print(f"Pizza 1: {unit_price(d1, p1):.2f} €/m²")
    print(f"Pizza 2: {unit_price(d2, p2):.2f} €/m²")
    print("Pizza 1 better value." if unit_price(d1, p1) < unit_price(d2, p2) else "Pizza 2 better value." if unit_price(
        d1, p1) > unit_price(d2, p2) else "Same value.")


if __name__ == "__main__":
    main()

def generate_fibonacci(n):
    fibs = []
    a, b = 0, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs


def save_to_file(numbers, filename="fibonacci.txt"):
    with open(filename, "w") as f:
        f.write("First 20 Fibonacci Numbers\n")
        f.write("==========================\n")
        for i, num in enumerate(numbers, start=1):
            f.write(f"{i:>2}. {num}\n")
    print(f"Saved {len(numbers)} Fibonacci numbers to '{filename}'")


if __name__ == "__main__":
    fibonacci_numbers = generate_fibonacci(20)
    print("Generated:", fibonacci_numbers)
    save_to_file(fibonacci_numbers)

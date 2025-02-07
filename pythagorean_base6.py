# Function to convert a number to base 6
def to_base6(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % 6))
        n //= 6
    return ''.join(str(x) for x in digits[::-1])

# Function to find Pythagorean triples
def pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2)**0.5
            if c.is_integer():
                triplets.append((a, b, int(c)))
    return triplets

# Function to display triples in base 6
def display_pythagorean_triplets_in_base6(limit):
    triples = pythagorean_triplets(limit)
    for a, b, c in triples:
        print(f"({to_base6(a)}, {to_base6(b)}, {to_base6(c)})")

# Run the function with a limit, e.g., 20
limit = 20
display_pythagorean_triplets_in_base6(limit)

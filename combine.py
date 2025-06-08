def print_lower_triangular(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("*" * i)
    print()  

def print_upper_triangular(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("*" * i)
    print()  

def print_pyramid(n):
    print("Pyramid Pattern:")
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)
    print()  

def get_positive_integer(prompt):
    while True:
        try:
            user_input = input(prompt)
            n = int(user_input)
            if n <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def main():
    print("\n" + "="*40)
    print("      Star Patterns Generator      ")
    print("="*40 + "\n")
    size = get_positive_integer("Enter the size of the patterns (positive integer): ")
    print()
    print_lower_triangular(size)
    print_upper_triangular(size)
    print_pyramid(size)

if __name__ == "__main__":
    main()











rows = int(input("Enter the number of rows: "))

print("\nLower Triangular Pattern:")
for i in range(1, rows + 1):
    print("* " * i)

print("\nUpper Triangular Pattern:")
for i in range(rows, 0, -1):
    print("* " * i)

print("\nPyramid Pattern:")
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '* ' * i
    print(spaces + stars)
























def lower_triangle(n):
    print("\nLower Triangular Pattern:")
    for i in range(1, n + 1):
        print(" ".join(["*"] * i))

def upper_triangle(n):
    print("\nUpper Triangular Pattern:")
    for i in range(n, 0, -1):
        print(" ".join(["*"] * i))

def pyramid(n):
    print("\nPyramid Pattern:")
    for i in range(1, n + 1):
        line = " " * (n - i) + " ".join(["*"] * i)
        print(line)

rows = int(input("Enter number of rows: "))

lower_triangle(rows)
upper_triangle(rows)
pyramid(rows)
















n = int(input("Enter the number of rows: "))

print("\nLower Triangular Matrix:")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()


print("\nUpper Triangular Matrix:")
for i in range(n):
    for j in range(n):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("\nPyramid Pattern:")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")  
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
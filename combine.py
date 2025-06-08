n = int(input("Enter the number of rows: "))

print("\nLower Triangular :")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()


print("\nUpper Triangular :")
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
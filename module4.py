# Read the integer N
N = int(input("Enter a positive integer N: "))

# Initialize an empty list to store the N numbers
numbers = []

# Read N numbers one by one
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Read the integer X
X = int(input("Enter an integer X to search: "))

# Check if X is in the list of numbers and output the result
if X in numbers:
    print(numbers.index(X) + 1)  # Output the 1-based index
else:
    print(-1)

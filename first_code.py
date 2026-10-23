
# My First Python Code
# Practicing basic Python concepts

# 1. Variables and data types
name = input("Enter your name: ")
# we use int to change user input in to integer
age = int(input("Enter your age: "))
height = 1.70
is_student = True

print("\n--- Personal Information ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# 2. Counting characters
print("\n--- Counting ---")
print("Number of characters in your name:", len(name))

# 3. Splitting a string
print("\n--- Split ---")
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Words:", words)
print("Number of words:", len(words))

# 4. Slicing a string
print("\n--- Slicing ---")
print("First three characters:", name[:3])
print("Last two characters:", name[-2:])

# 5. If-else condition
print("\n--- Age Check ---")
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

# 6. Basic data type checks
print("\n--- Data Types ---")
print("name:", type(name))
print("age:", type(age))
print("height:", type(height))
print("is_student:", type(is_student))

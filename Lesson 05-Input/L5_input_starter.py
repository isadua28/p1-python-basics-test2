# LESSON 5: USER INPUT & PROCESSING
# print("LESSON 5: USER INPUT & PROCESSING (Advanced Track)")
# print("=" * 50)

# PART 1: Input Comparison (JS vs Python)
# print("\n--- PART 1: Input Comparison ---")
# # Compare to JS: let name = prompt("Name:");
# name = input("Name: ")
# print(f"Hello, {name}")

# Compare to JS: let age = parseInt(prompt("Age:"));
# age = int(input("Age: "))
# print(f"You are {age} years old.")

# PART 2: Type Conversion - Python Style  
print("\n--- PART 2: Type Conversion ---")
# # Like JS parseInt(), parseFloat() but Python syntax
# num_str = "42"
# num_int = int(input(num_str))
# num_float = float(input(num_str))
# print(type(num_str)) is still a string 

# print(f"You are {int(num_str)} years old.")
# # Try the bool() function - different from JS truthy/falsy
# print(f"bool(''): {bool('')}")  # False
# print(f"bool(0): {bool(0)}")    # False 
# print(f"bool(-10): {bool(-10)}")# True
# print(f"bool(' '): {bool(' ')}")# True
# Only empty strings and zeroes give you false

# PART 3: Math Operators (Focus on differences from JS)
print("\n--- PART 3: Math Operators ---")
# Test regular division / (always returns float in Python)
print(f"6 / 2 = {6/2} (type: {type(6/2)})")     # Float
print(f"6 // 2 = {6//2:.5f} (type: {type(6//2)})")  # Floor

# Test floor division // (doesn't exist in JS)

# Test with same numbers - see the difference
print(f"6 // 2 = {6//2} (type: {type(6//2)})")  # Yields to an integer 

# PART 4: Complex Expressions & Precedence
print("\n--- PART 4: Complex Expressions ---") 
# Test: 9 + 6 / 3 * 2 - 1 (same rules as JS?) 
result = 9 + 6 / 3 * 2 - 1
print(f"9 + 6 / 3 * 2 - 1 = {result}")
print("9 + 2.0 * 2 - 1") # Division first
print("9 + 4.0 - 1") # Multiplication
print("12.0") # Addition + Subtraction 

# Test: 6 / 2 (what type is the result?)
print(6 / 2) # float

user_name = input("Name: ")
fav_num = int(input("Favorite Number: "))
fav_num_double = int(fav_num * 2)
print(f"Hello {user_name}, your favorite number is {fav_num}, and that times 2 is {fav_num_double}!")
# Create a function that returns the factorial of any positive input number
# Helpful tip: Try to solve the problem comfortably in code before trying it recursively!
# Factorial is:
# 4! ==> 4 x 3 x 2 x 1

# Tip:
# 1.) Solution
# 2.) Methodology
# 3.) Plan

# Declare function
def factorial(n):
    # factorial of 1
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Input a positive number"
    return n * factorial(n - 1)

num_input = int(input("Enter an integer: "))
print(factorial(num_input))
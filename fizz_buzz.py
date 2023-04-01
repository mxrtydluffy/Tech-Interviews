# Question

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

#_________________________________________________________________________________________________________________________________#

# Example 1
# Input: n = 3
# Output: ["1","2","Fizz"]

def fizzBuzz(n):
    for i in range(n + 1):
        if ((i%3==0) and (i%5==0)):
            print("FizzBuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("Buzz")
        else:
            print(str(i))

fizzBuzz(15)

#                          Pseudocode
# Begin by creating a function that takes in a number in this case n.
# Then reiterate in the index so the the number increases from 1.
# Within for loop have one if loop that checks if index is divisible by 5 and 3, if som print FizzBuzz
# If not true check if divisible by 3. If so print Fizz.
# If not true again check if divisible by 5. If true print Buzz.
# At the end it returns a string of the index.
# Lastly, call function and put arguement to get desired output.
# Algorithm for finding the largest number from different numbers
# 1. Compare the first number to the second one. the larger number is now the largest number
# 2. If there is another number to comparek, take the largest number and compare it to the next number, the larger number is now the largest number.
# 3. Repeat step 2 until there are no more numbers left to compare
# 4. Your largest number will be the larger number of the last comparison

#Code implementation for finding the largest number
num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int
while num_int > 0:
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line

#Algorithm for a sequence
# 1. Initialize with 1, 2 and 3 as the first three numbers
# 2. To find the next number add the last three together
# 3. shift the 3 numbers down one place and make the sum of them the 3rd number.  
# 4. Repeat step 2 and 3 for n-3 times
n = int(input("Enter the length of the sequence: ")) # Do not change this line
first_num = 1
second_num = 2
third_num = 3
print("1")
print("2")
print("3")
for x in range(n-3):
    sum = first_num + second_num + third_num
    print(sum)
    first_num = second_num
    second_num = third_num
    third_num = sum
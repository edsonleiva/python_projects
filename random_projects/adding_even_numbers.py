###### ADDING EVEN NUMBERS ######

# Enter the stopping digit
num_list = int(input('Enter a number: '))

# placeholder for sum
sum = 0

# this loop will add all even numbers up to the stopping digit
for num in range(0, num_list + 1):
    if num % 2 == 0:
        sum += num
    else:
        continue

# print the sum
print(sum)
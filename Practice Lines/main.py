

# Multiplying the numbers in the list by two in 5 lines
numbers = [1, 3, 5, 7, 9]
doubled_numbers = []
for num in numbers:
  doubled_numbers.append(num*2)
print(doubled_numbers)


# Multiplying the numbers in the list by two in 3 lines
numbers = [1, 3, 5, 7, 9]
doubled_numbers = [num*2 for num in numbers]
#adding more conditions here
# doubled_numbers = [num*2 for num in numbers if num > 3] 
print(doubled_numbers)

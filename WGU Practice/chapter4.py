
# Practice 1 - Enter 100
# A half-life is the amount of time it takes for a substance or entity to fall to half its original value. 
# Caffeine has a half-life of about 6 hours in humans. Given caffeine amount ( in mg) as input, 
# output the caffeine level after 6, 12, and 24 hours. Use a string formatting expression with conversion specifiers 
# to output the caffeine amount as floating-point numbers.
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('{:.2f}'.format(your_value))


caffeine_mg = float(input())
six_hours = caffeine_mg / 2
twelve_hours = six_hours / 2
twenty_four_hours = twelve_hours / 4

print('After 6 hours: {:.2f}'.format(six_hours),'mg')
print('After 12 hours: {:.2f}'.format(twelve_hours),'mg')
print('After 24 hours: {:.2f}'.format(twenty_four_hours),'mg')


# Practice 2 - Enter 200000, 210000
current_price = int(input())
last_months_price = int(input())

diff_price = current_price - last_months_price
payment = (current_price * 0.051)/12

# print("This house is $",'{:.2f}'.format(current_price),".","The change is $-",'{:.2f}'.format(diff_price),"since last month.")
# print("The estimated monthly mortgage is",'{:.2f}'.format(payment),".")

print('This house is ${}. The change is ${} since last month.'.format(
    current_price, diff_price))
print('The estimated monthly mortgage is ${:.2f}.'.format(payment))


# Practice 3 - Enter 8.3, 10.4, 5.0, 4.8

# Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers
# to output their product and their average as integers (rounded), then as floating-point numbers.
# Output each rounded integer using the following:
# print('{:.0f}'.format(your_value))
# Output each floating-point value with three digits after the decimal point,
# which can be achieved as follows:
# print('{:.3f}'.format(your_value))

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4)/4

print('{:.0f} {:.0f}'.format(product, average))
print('{:.3f} {:.3f}'.format(product, average))



# Practice 1 - Enter 2000, 2
import math
user_num = int(input())
x = int(input())
result = user_num // x
print(result, end=" ")
result = result // x
print(result, end=" ")
result = result // x
print(result)


# Practice 2 - Enter 49, 155, 148, 60
''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

age_years = int(input())
weight_pounds = int(input())
heart_bpm = int(input())
time_minutes = int(input())

calories_man = ((age_years * 0.2017) + (weight_pounds * 0.09036) +
                (heart_bpm * 0.6309) - 55.0969) * time_minutes / 4.184
calories_woman = ((age_years * 0.074) - (weight_pounds * 0.05741) +
                  (heart_bpm * 0.4472) - 20.4022) * time_minutes / 4.184

print('Women: {:.2f} calories'.format(calories_woman))
print('Men: {:.2f} calories'.format(calories_man))


# Practice 3 - 5.0, 1.5, 3.2

# #Given three floating-point numbers x, y, and z,
# output x to the power of z,
# x to the power of (y to the power of z),
# the absolute value of (x minus y),
# and the square root of (x to the power of z).
# # Output each floating-point value with two digits after
# the decimal point, which can be achieved as follows:
# print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))

x = float(input())
y = float(input())
z = float(input())

power = pow(x, z)
power_two = x**y**z
absole = math.fabs(x-y)
square = math.sqrt(x ** z)

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(power, power_two, absole, square))


# Practice 4 - Enter 440

# On a piano, a key has a frequency, say f0.
# Each higher key (black or white) has a frequency of f0 * rn,
# where n is the distance (number of keys) from that key, and r is 2(1/12).
# Given an initial key frequency, output that frequency and the next 4 higher key frequencies.

# Output each floating-point value with two digits after the decimal point,
# which can be achieved as follows:
# print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4, your_value5))
# Note: Use one statement to compute r = 2(1/12) using the pow function(remember to import the math module). 
# Then use that r in subsequent statements that use the formula fn = f0 * rn with n being 1, 2, 3, and finally 4.


initial_frequency = float(input())
r = 2 ** (1/12)
next_frequencies = [initial_frequency * (r ** n) for n in range(5)]
# print(f'{initial_frequency:.2f}')
for frequency in next_frequencies:
    print(f'{frequency:.2f}')


import math


def if_power_of_3_1(n):
    a = math.log(n,3)
    print(n, a, a % 1, end=' ')
    return not a % 1


def if_power_of_3(input_param):
    print(input_param, end=' ')
    return not input_param - pow(round(pow(input_param, 1/3)),3)


print(if_power_of_3(pow(1,3)))
print(if_power_of_3(pow(2,3)))
print(if_power_of_3(pow(3,3)))
print(if_power_of_3(50))
print(if_power_of_3(pow(4,3)))
print(if_power_of_3(pow(34,3)))
print(if_power_of_3(2134787234089))
print(if_power_of_3(pow(2134787234089,3)))
print(if_power_of_3(487287348723))
print(if_power_of_3(pow(487287348723,3)))
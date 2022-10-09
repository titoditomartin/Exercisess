#Febrian Martin Herdito - L1BC


#1
# r = float(input("Enter radius "))
# area = r*r*3.14
# print("The area of the circle is", area)

#2
# firstName = str(input("Enter first name "))
# lastName = str(input("Enter last name "))
# print(lastName,firstName,sep=" ")

#3
# color_list = ["Red","Green","White","Black"]
# print(color_list[0], color_list[-1])

#4
# x = int(input("Enter a number" ))
# n1 = int( "%s" % x )
# n2 = int( "%s%s" % (x,x) )
# n3 = int( "%s%s%s" % (x,x,x) )
# print (n1+n2+n3)

#5
# pi = 3.14
# r = 6
# vol = 4/3 * pi * r**3
# print("The value of the volume is", vol)

#6-
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
# print(difference(30))
# print(difference(20))

#7-
# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))

#8
# number = int(input("Enter a number "))
# if number % 2 == 0:
#         print("The number is even")
#
# else:
#         print("The number is odd")

#9-
# l = input("Input a letter of the alphabet: ")
# if l in ('a', 'e', 'i', 'o', 'u'):
#  	print("%s is a vowel." % l)
# else:
#  	print("%s is a consonant." % l)

#10-
# def is_group_member(group_data, n):
#  return n in group_data
# print(is_group_member([2, 1, 9, 3], 3))
# print(is_group_member([5, 6, 7], -10))

#11-
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)
# histogram([3, 4, 5, 6])

#12-
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#             399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#             815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#             958,743, 527]
# for x in numbers:
#     if x %2 == 0:
#         print(x)

#13
# b = float(input("Enter base number of a triangle: "))
# h = float(input("Enter height number of a triangle: "))
# area = b*h/2
# print("The value of the triangle area is", area)

#14--
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))

#15-
# def sum_three(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum_three(10, 9, 2))
# print(sum_three(5, 2, 2))

#16-
# x, y = 4, 3
# result = x * x + 2 * x * y + y * y
# print("({} + {}) ^ 2) = {}".format(x, y, result))

#17--
# amt = 10000
# int = 3.5
# years = 7
# future_value = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))

#18--
# import math
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
# print(distance)

#19-
# n = int(input("Input a number: "))
# sum_num = (n * (n + 1)) / 2
# print("Sum of the first", n ,"positive integers:", sum_num)

#20-
# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))

# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)

# print("Your height is : %d cm." % h_cm)

#21-
# from math import sqrt
# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is:", c )

#22--
# height = float(input("Input your height in Feet: "))
# weight = float(input("Input your weight in Kilogram: "))
# print("Your body mass index is: ", round(weight / (height * height), 2))

#23---
# print('\nCalculate the midpoint of a line:')
#
# x1 = float(input('The value of x (the first endpoint) '))
# y1 = float(input('The value of y (the first endpoint) '))
#
# x2 = float(input('The value of x (the first endpoint) '))
# y2 = float(input('The value of y (the first endpoint) '))
#
# x_m_point = (x1 + x2)/2
# y_m_point = (y1 + y2)/2
# print();
# print("The midpoint of line is :")
# print( "The midpoint's x value is: ",x_m_point)
# print( "The midpoint's y value is: ",y_m_point)
# print();

#24--
# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))
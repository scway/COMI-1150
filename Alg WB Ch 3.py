# # 1. Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable z if the
# # variable x is greater than 100
# x = int(input('x= '))
# y = 20
# z = 0
# if x > 100:
#     z = 40
# print('y= ', y)
# print('z= ', z)
#
# # 2. Write an if statement that assigns 0 to the variable b, and assigns 1 to the variable c
# # if the variable a is less than 10.
# a = int(input('a= '))
# b = 0
# c = 0
# if a <= 10:
#     c = 1
# print('a= ', a)
# print('b= ', b)
# print('c= ', c)
#
# # 3. Write an if-else statement that assigns 0 to the variable b if the variable a is less
# # than 10. Otherwise, it should assign 99 to the variable b.
#
# a = int(input('a = '))
# if a < 10:
#     b = 0
# else: b = 99
# print('b = ', b)
#
# # 4. The following code contains several nested if-else statements. Unfortunately, it
# # was written without proper alignment and indentation. Rewrite the code and use the
# # proper conventions of alignment and indentation.
# if score >= A_score:
#     print('Your grade is A.')
# else:
#     if score >= B_score:
#         print('Your grade is B.')
#     else:
#         if score >= C_score:
#             print('Your grade is C.')
#         else:
#             if score >= D_score:
#                 print('Your grade is D.')
#             else:
#                 print('Your grade is F.')
#
# # 5. Write nested decision structures that perform the following: If amount1 is greater than
# # 10 and amount2 is less than 100, display the greater of amount1 and amount2
#
# amount1 = int(input('Choose a numerical amount: '))
# amount2 = int(input('Choose another numerical amount: '))
#
# if amount1 > 10:
#     if amount2 < 100:
#         if amount1 > amount2:
#             print(amount1)
#         elif amount2 > amount1:
#             print(amount2)
#         elif amount1 == amount2:
#             print('The amounts are equal.')
#
#6. Write an if-else statement that displays 'Speed is normal' if the speed variable is
#within the range of 24 to 56. If the speed variable’s value is outside this range, display
#'Speed is abnormal'.
#
# speed = int(input('What is the speed?: '))
# if speed >= 24 and speed <= 56:
#     print('Speed is normal.')
# else:
#     print('Speed is abnormal.')
#7. Write an if-else statement that determines whether the points variable is outside
#the range of 9 to 51. If the variable’s value is outside this range it should display
#“Invalid points.” Otherwise, it should display “Valid points.”
#
# variable = int(input('What is the variable?: '))
# if variable >= 9 and variable <= 51:
#     print('Valid points.')
# else:
#     print('Invalid points.')
'''
----------------------------------
|     💻 Exercises - Day 3       |
----------------------------------
'''
# settings.json生效
from sympy import Eq, symbols, solve
from math_tools import solve_quadratic_equation


# Declare your age as integer variable
AGE = 15
print(type(AGE))
# Declare your height as a float variable
HEIGHT = 175.0
print(type(HEIGHT))
# # Declare a variable that store a complex number
CPLXNB = 1+3j
print(type(CPLXNB))
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
BASE = input("Please enter the base : ")
HEIGHT = input("Please enter the height: ")
AREA = 0.5*float(BASE)*float(HEIGHT)
print(AREA)
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
A = input("Please enter the side a : ")
B = input("Please enter the side b : ")
C = input("Please enter the side c : ")
PERIMETER = int(A) + int(B) + int(C)
print(PERIMETER)


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input("pleae enter the length of a rectangle :")
width = input("pleae enter the width of a rectangle :")
AREA = float(length) * float(width)
PERIMETER = 2 * (float(length) + float(width))
print("area of the rectangle is ", AREA)
print("PERIMETER of the rectangle is ", PERIMETER)
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input("pleae enter the radius of a circle :"))
PI = 3.14
AREA = round(PI * r * r, 2)
c = 2 * r * r
print("area of the circle is ", AREA)
print("circumference of the circle is ", c)


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# 定义符号变量
x, y = symbols('x y')
equation = Eq(y, 2*x - 2)
slope = 2
# 解方程 y = 0，得到 x 轴截距
x_intercept = solve(equation.subs(y, 0), x)[0]
# 解方程 x = 0，得到 y 轴截距
y_intercept = solve(equation.subs(x, 0), y)[0]
# 打印结果
print("方程：", equation)
print("斜率：", slope)
print("x 轴截距：", x_intercept)
print("y 轴截距：", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
pnt = [(2, 2), (6, 10)]
x1, y1 = pnt[0]
x2, y2 = pnt[1]
m = round(y2-y1/x2-x1, 2)
print("slope is :", m)

# Compare the slopes in tasks 8 and 9.

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
root = solve_quadratic_equation(1, 6, 9)
print(root)


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
STR1 = len('python')
STR2 = len('dragon')

if STR1 == STR2:
    print("长度相同")
else:
    print("异常")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if ('on' in 'python') and ('on' in 'dragon'):
    print("包含on")
else:
    print("至少一个单词不包含")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if ('jargon' in 'I hope this course is not full of jargon.'):
    print('jargon包含在句子中')
else :
    print('啥都不是')
# There is no 'on' in both dragon and python
if ('on' in 'dragon and python'):
    print('不存在')
else :
    print('太阳从西边出来')

# Find the length of the text python and convert the value to float and convert it to string
print('python这个单词的字母长度为 ：',len('python'))
print(type(float(len('python'))))
print(type(str(len('python'))))


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def is_even(number):
    '''

    这个方法用来计算是否为偶数

    '''
    if (number % 2 == 0):
        return '这是偶数'
    else:
        return '这是奇数'


print(is_even(7))
print(is_even(10))
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.


# Check if type of '10' is equal to type of 10
print(isinstance('10', str) == isinstance(10, int))
print(isinstance('10', str))
print(isinstance(10, float))


# Check if int('9.8') is equal to 10
print(int(9.8))
print(int(9.8)==10)


# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('请输入小时数： '))
rate = int(input('请输入平均工资： '))
print('人工费用需要支付：  ', rate * hours)


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('please enter the number of years :'))
sec=years*365*86400
print('You have lived for',sec, 'seconds.')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
display_table(5)

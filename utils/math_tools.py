'''
这个文件放的都是数学公式
'''
import math

def solve_quadratic_equation(a, b, c):
    '''
    方法名称：solve_quadratic_equation
    功能：计算二元一次方程的不同的实数根
    参数：a,b,c
    返回值：方程的实数根
        
    '''
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return None  # 返回 None 表示没有实数根（虚根）

def display_table(rows):
    '''
    按照要求打印表格内容
    # 1 1 1 1 1
    # 2 1 2 4 8
    # 3 1 3 9 27
    # 4 1 4 16 64
    # 5 1 5 25 125

    '''
    for i in range(1, rows+1):
        print(f"{i} {1} {i} {i**2} {i**3}")
        
#解一元二次方程
def solve_quadratic_equation(a,b,c):
    if a == 0:
        print('二次项系数为0,该方程不能成立')
        exit()
    from math import sqrt
    detla = b**2 - 4*a*c
    if detla < 0:
        return False
    elif detla == 0:
        return -(b / (2 * a))
    else:
        sqrt_detla = sqrt(detla)
        x1 = (-b + sqrt_detla) / (2 * a)
        x2 = (-b - sqrt_detla) / (2 * a)
        return x1,x2

if __name__ == '__main__':
    coefficient_name = ['二次项','一次项','常数项']
    coefficient_numbers = []
    for items in coefficient_name: 
            equation = input('请分别输入%s的系数' %(items))
            coefficient_numbers.append(float(equation))
    coefficient_name.pop(0)
    print('您输入的系数分别为%s' %(coefficient_numbers))
    a,b,c = coefficient_numbers
    roots = solve_quadratic_equation(a,b,c)
    if roots:
        print('该方程的解是',roots)
    else:
        print('这个方程没有解')

        
# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.



dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def rgb(r, g, b):
    res_r = convert(r)
    res_g = convert(g)
    res_b = convert(b)
    result = f'{res_r}{res_g}{res_b}'
    return result


def convert(a):
    if a > 255:
        a = 255
    elif a < 0:
        a = 0
    elif a in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        a = f'0{a}'
        return a

    first_res = a//16
    second_res = a % 16
    if first_res > 10:
        first_res = dict[first_res]
    if second_res > 10:
        second_res = dict[second_res]
    return f'{first_res}{second_res}'


print('Should be: 000000', 'realy: ', rgb(0, 0, 0))
print('Should be: 010203', 'realy: ', rgb(1, 2, 3))
print('Should be: FFFFFF', 'realy: ', rgb(255, 255, 255))
print('Should be: FEFDFC', 'realy: ', rgb(254, 253, 252))
print('Should be: 00FF7D', 'realy: ', rgb(-20, 275, 125))

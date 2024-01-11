# 有使用chatgpt並稍微修改

import numpy as np

def solve_polynomial():
    try:
        coefficients_input = input("輸入係數 (以空格分開): ")
        
        coefficients = [float(x) for x in coefficients_input.split()]

        roots = np.roots(coefficients)

        print("x = ", roots)
    except ValueError:
        print("error try again!!")

solve_polynomial()
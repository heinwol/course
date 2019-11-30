import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.interactive import printing
from sympy.parsing.sympy_parser import parse_expr
from sympy.printing.latex import latex
import typing

x = sp.symarray('x', 5)
#C, P, R, T == x[1], x[2], x[3], x[4] respectively

xpr = parse_expr
some_var = 606

#equation parameters
k_c, mu_c,     C_0,     lambda_c, K_c      = sp.symbols("k_c, mu_c, C_0, lambda_c, K_c")
k_p, mu_p,     K_p,     P_0,      lambda_p = sp.symbols("k_p, mu_p, K_p, P_0, lambda_p")
k_r, lambda_r, gamma_p, gamma_c            = sp.symbols("k_r, lambda_r, gamma_p, gamma_c")
k_t, K_t,      lambda_t                    = sp.symbols("k_t, K_t, lambda_t")

params = {'C_0' : 10**6, 'P_0' : 10**5,'k_c' : 7.5e-2, 'K_c' : 0.1, 'lambda_c' : 10**(-7), \
    'k_p' : 0.2, 'lambda_p' : 0.15, 'k_r' : 0.2, 'lambda_r' : 0.22, 'k_t' : 3300, 'lambda_t' : 0.3}
params['mu_c'] = 20*params['k_c'] / params['P_0']
params['mu_p'] = 20*params['k_p']
params['K_p'] = params['C_0'] / 100
params['gamma_p'] = 0.02 * params['lambda_r'] / (params['P_0'] * (1 - params['lambda_p'] / params['k_p']))
params['gamma_c'] = params['gamma_p']
params['K_t'] = params['K_c']

# f1 = (k_c + mu_c*x[2]) * x[1]**(3/4) * (1 - (x[1]/C_0)**(1/4) ) - \
#         (lambda_c * x[1]*x[4]) / (K_c + 1 - x[3])
# f2 = x[2] * (1 - x[2] / P_0) * (k_p + mu_p*x[1] / (K_p + x[1]) ) - lambda_p*x[2]
# f3 = k_r - x[3] * (lambda_r + gamma_p*x[2] + gamma_c*x[1])
# f4 = k_t*x[3] / (K_t - x[3] + 1) - lambda_t*x[4]

f1 = (k_c + mu_c*x[2]) * x[1]**xpr("3/4") * (1 - (x[1]/C_0)**xpr("1/4") ) - \
        (lambda_c * x[1]*x[4]) / (K_c + 1 - x[3])
f2 = x[2] * (1 - x[2] / P_0) * (k_p + mu_p*x[1] / (K_p + x[1]) ) - lambda_p*x[2]
f3 = k_r - x[3] * (lambda_r + gamma_p*x[2] + gamma_c*x[1])
f4 = k_t*x[3] / (K_t - x[3] + 1) - lambda_t*x[4]

F = sp.Matrix([f1, f2, f3, f4])


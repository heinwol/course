import sympy as sp
import numpy as np
import matplotlib
from sympy.interactive import printing
from sympy.parsing.sympy_parser import parse_expr
from sympy.printing.latex import latex
import typing
from IPython.display import Latex

#printing.init_printing(use_latex=True)
#sp.init_session()

xpr = parse_expr


def grad(f, elts):
    nabla_f = sp.Matrix([0]*len(elts)).T
    # sp.transpose(nabla_f)
    for i in range(len(elts)):
        nabla_f[i] = sp.diff(f, elts[i])
    return nabla_f

class Eqn(sp.Eq):
    def __new__(cls, *args, **kwargs):
        instance = super(Eqn, cls).__new__(cls, *args, **kwargs)
        return instance

    def __mul__(self, expr):
        left = self.lhs * expr
        right = self.rhs * expr
        return Eqn(left, right)

    def __add__(self, expr):
        left = self.lhs + expr
        right = self.rhs + expr
        return Eqn(left, right)

    def __sub__(self, expr):
        left = self.lhs - expr
        right = self.rhs - expr
        return Eqn(left, right)

    def __truediv__(self, expr):
        left = self.lhs / expr
        right = self.rhs / expr
        return Eqn(left, right)

    def __pow__(self, expr):
        left = self.lhs ** expr
        right = self.rhs ** expr
        return Eqn(left, right)

def flatex(text: str, *args):
    return Latex(text.format(sp.latex(args, mode='plain')))

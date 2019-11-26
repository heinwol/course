import sympy as sp
from sympy.printing.latex import latex
from IPython.display import Latex

def flatex(text: str, *args):
    return Latex(text.format(sp.latex(args, mode='plain')))

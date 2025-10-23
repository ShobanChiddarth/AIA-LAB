from sympy import symbols
from sympy.logic.boolalg import Implies, And, Not, Equivalent, Or


P, Q = symbols("P Q")
P = True
Q = False


print("P ∧ Q =", And(P, Q))
print("P ∨ Q =", Or(P, Q))
print("¬Q =", Not(Q))
print("P → Q =", Implies(P, Q))
print("P ↔ Q =", Equivalent(P, Q))
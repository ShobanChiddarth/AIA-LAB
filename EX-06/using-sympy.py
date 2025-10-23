from sympy import satisfiable, symbols
from sympy.logic.boolalg import Implies, And, Not

P, Q = symbols("P Q")

KB = And(Implies(P, Q), P)

query = Q

result = not satisfiable(And(KB, Not(query)))

print("Does KB entail Q?", result)

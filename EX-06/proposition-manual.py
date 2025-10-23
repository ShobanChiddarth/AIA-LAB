

def implies(p, q):
    return (not p) or q

def iff(p, q):
    return (p and q) or (not p and not q)

# propositional statements
d = {
    "P": True,
    "Q": False,
    "R": True
}


print("--- Propositional Logic Evaluation ---")

print("P ∧ Q =", d["P"] and d["Q"])
print("P ∨ Q =", d["P"] or d["Q"])
print("¬Q =", not d["Q"])
print("P → R =", implies(d["P"], d["R"]))
print("P ←→ R =", iff(d["P"], d["R"]))

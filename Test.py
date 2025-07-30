import tellurium as te
r = te.loada("""
    A -> B; k1*A
    B -> C; k2*B
    A = 10; B = 0; C = 0;
    k1 = 1; k2 = 0.5
""")
result = r.simulate(0, 10, 100)
r.plot(result)

from pyqubo import Binary
x0, x1, x2, x3, x4, x5, x6 = Binary('x0'), Binary('x1'),Binary('x2'), Binary('x3'),Binary('x4'), Binary('x5'), Binary('x6')
H = 6*x0 + x1 + 4*x2 - 23*x3 - 7*x4 + 8*x5 - 9*x6 + 3*x0*x2 - 23*x1*x2 - 7*x0*x1 + 2*x0*x3 + 3*x4*x2 + 22*x1*x5 + 334*x1*x3 - 3*x3*x4 - 3*x5*x2 + 5*x2*x3
pprint(H.compile().to_qubo()) 
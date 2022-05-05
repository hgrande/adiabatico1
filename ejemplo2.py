# Importamos las funciones y paquetes que vamos a usar
from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

# Define the problem as a Python dictionary and convert it to a BQM
Q = {('B','B'): 1,
    ('K','K'): 1,
    ('A','C'): 2,
    ('A','K'): -2,
    ('B','C'): -2}

# Convert the problem to a BQM
bqm = BinaryQuadraticModel.from_qubo(Q)

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample(bqm,
                           num_reads = 10,
                           label='Example - Simple Ocean Programs: BQM')
print(sampleset)

# EL modelo QUBO es una función objetivo de variables binarias representadas como una matriz diagonal superior,
# donde los términos de la digonal son los coeficientes lineales y los términos no nulos de fuera de la diagonal son los coeficientes cuadráticos.

#    E(x) = sumatorio xi * Qi,j * xj               xi € {0,1}
#             i<=j  
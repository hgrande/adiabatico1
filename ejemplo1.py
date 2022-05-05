from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

Q = {('B','B'): 1,('K','K'): 1,('A','C'): 2,('A','K'): -2,('B','C'): -2} #Definimos el problema como un  diccionario de Python

bqm = BinaryQuadraticModel.from_qubo(Q) #Lo convertimos a un QUBO

# Convertimos el bqm a un modelo Ising 
ising_model = bqm.to_ising()

# Definimos el sampler que usaremos para ejecutar el problema
sampler = EmbeddingComposite(DWaveSampler())

#Ejecutamos el problema en el sampler
sampleset = sampler.sample_ising(
                h = ising_model[0],
                J = ising_model[1],
                num_reads = 10,
                label='Example - Simple Ocean Programs: Conversion')

#ponemos el resultado en pantalla
print(sampleset)
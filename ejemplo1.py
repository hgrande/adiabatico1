# El SDK de Ocean provee una estructura de modelo cuadrático binario (BQM) para almacenar y subir problemas a la unidad de procesador cuántico  (QPU).
# Este programa ejecuta un problema Ising ( de un BQM) en la QPU de Dwave
from dwave.system import EmbeddingComposite, DWaveSampler
# La clase dimod.binaryQuadraticModel puede contener tanto modelos QUBO como modelos Ising 
# y sus métodos proveen utilidades para trabajar con ellos y entre las dos representaciones de un problema.
from dimod import BinaryQuadraticModel 

Q = {('B','B'): 1,('K','K'): 1,('A','C'): 2,('A','K'): -2,('B','C'): -2} #Definimos el problema como un  diccionario de Python

bqm = BinaryQuadraticModel.from_qubo(Q) #Lo convertimos a un BQM

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

# BQM (Binary Quadratic Model) y es el término genral que abarca problemas Ising y problemas QUBO.

# La clase  modelo cuadrático binario (BQM) codifica modelos Ising y modelos quadratic unconstrained binary optimization (QUBO) usados por 
# samplers tales como el sistema  D-Wave .

# Ecuación BQM :        

#    E(v) = sumatorio (ai*vi) + sumatorio(bi,j*vi*vj) + c      vi € {-1,+1} o {0,1}
#               i=1               i<j


The BQM equation,
# El software Ocean (librerías para ejecutar problemas en los ordenadores cuánticos de D-Wave) acepta tanto problemas Ising como problemas QUBO,
# pero se requieren banderas que indiquen si nos interesa una solución "BINARIA" (QUBO) o  "SPIN" (Ising) .
# Las expresiones para un problema Ising o para un problema QUBO son muy similares. En realidad, las expresiones Ising y QUBO son isomorfas.

# El modelo Ising es una función objetivo de N variables s = [s1,...,sN] correspondientes a los spin físicos de Ising , donde hi son las bias 
# y Ji,j los acopladores (interacciones) entre spins:

#       Ising:     E(s) = sumatorio (hi*si) + sumatorio(Ji,j*si*sj) 
#                             i=1                i<j

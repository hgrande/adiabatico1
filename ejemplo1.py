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


# Diferencias entre Ising y QUBO : evidentemente , la mayor diferencia es que Ising trabaja con spin (-1,1) y QUBO usa binario(0,1).
# Dado que ambas expresiones son isomorfas, la elección de  spin o binario puede afectar la manera de expresar el problema;
# es decir, por qué QUBOs pueden ser totalmente expresados en forma  expanded y matricial,mientras Ising puede ser expresado en forma expandida,
# pero no puede ser expresado totalmente en forma matricial. Consideremos la siguiente multiplicación de matrices :

#                  1  4  6   x1
# (x1   x2    x3)( 0  2  5 )(x2 )      2**
#                  0  0  3   x3

# Expandiendo (resolviendo) esta multiplicación obtenemos  x1^2 + 2x2^2 + 3x3^2 + 4x1x2 + 5x2x3 + 6x1x3    2**

# Recordemos que podemos expresar tanto Ising como QUBO en la siguiente expresión expandida : x1 + 2x2 + 3x3 + 4x1x2 + 5x2x3 + 6x1x3    1**
# Recordemos también que con QUBOs, solo trabajamos con variables binarias, 0s y 1s. Por lo tanto , si tenemos un xi perteneciente al conjunto {0,1}, 
# entonces xi = xi^2. (i.e. 0=0^2 and 1=1^2). Esto significa que un problema QUBO expresado como en 2** puede ser expresado también como 1**  :
# 
#                                                                                                             1  4  6   x1
#    x1 + 2x2 + 3x3 + 4x1x2 + 5x2x3 + 6x1x3 = x1^2 + 2x2^2 + 3x3^2 + 4x1x2 + 5x2x3 + 6x1x3 = (x1   x2    x3)( 0  2  5 )(x2 ) 
#                                                                                                             0  0  3   x3

# Pero esta propiedad x_i = x_i^2 no se cumple para spins, ya que -1 no es igual a  (-1)^2.
# Por lo tanto , el problema Ising no puede ser escrito totalmente  en forma matricial , porque 
#  x1 + 2x2 + 3x3 + 4x1x2 + 5x2x3 + 6x1x3 es distinto de  x1^2 + 2x2^2 + 3x3^2 + 4x1x2 + 5x2x3 + 6x1x3
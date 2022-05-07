from pyqubo import Binary #Trabajamos en binario 
x0, x1, x2, x3, x4, x5, x6 = Binary('x0'), Binary('x1'),Binary('x2'), Binary('x3'),Binary('x4'), Binary('x5'), Binary('x6')
H = 6*x0 + x1 + 4*x2 - 23*x3 - 7*x4 + 8*x5 - 9*x6 + 3*x0*x2 - 23*x1*x2 - 7*x0*x1 + 2*x0*x3 + 3*x4*x2 + 22*x1*x5 + 334*x1*x3 - 3*x3*x4 - 3*x5*x2 + 5*x2*x3
print(H.compile().to_qubo())   #Hasta aquí, al ejecutar obtenemos la funciòn objetivo . (Definición del Hamiltoniano) 

M = 6  #Buscaremos M (el peso de penalización o peso de la restricción en nuestro problema).Creamos, por tanto, un QUBO con diferentes valores de M para ver cuál es más óptimo . En nuestro ejemplo probamos con M=5 y M= 6 

s_0, s_1 = Binary('s_0'), Binary('s_1') #Como la primera restricción es una desigualdad, necesitamos variables auxiliares para convertirla en igualdad. 


# defining the constraint
const_1 = 0

for i in range(7): #Recordemos que en nuestro problema tenemos 7 variables
    const_1 +=x[i]
    
const_1 += -s_0 - 2*s_1 - 3  #La restricción es > , luego tendremos que restar las variables de holgura para convertirlo en = (si fuera < , las sumaríamos) 
    
#Nuestra función de coste será la función Q definida arriba , pero añadiendo ahora la restricción(elevada al cuadrado, para evitar valores negativos de la misma) 
Q += Constraint(const_1**2, label='const_1')

#Pasamos ahora a trabajar la segunda restricción . Llamamos P al penalty de esta segunda restricción(lo que era M en la primera)
P = Placeholder('P') #Si usamos placeholder, podemos cambiar el valor de P sin tener que compilar cada vez. Así podemos ir modificando el peso de la restricción de forma más dinámica

const_2 = 0

for i in range(5): #Nuestra segunda restricción considera los valores x[i] y x[i+2] y tenemos un total de 7 variables, desde x[0] hasta x[7] , con lo cual i como mucho puede llegar hasta 5 porque 5+2 = 7
    const_2 += x[i]*x[i+1]
#Implementamos nuestra función de coste ya con la segunda restricción incluida(como explicamosantes, también elevada al cuadrado)    
Q += Constraint(const_2**2, label='const_2')

#Compilamos probando con el valor P = 8 e imprimimos el resultado en pantalla : 
model = Q.compile()
qubo, offset = model.to_qubo(feed_dict={'P': 7})

print('The qubo is:', qubo)
print('\nThe offset is:', offset)

# Vemos el resultado gráficamente : 

bqm = dimod.BinaryQuadraticModel.from_qubo(qubo,offset)

G = dimod.to_networkx_graph(bqm)
plt.figure(figsize=(6, 6))
nx.draw(G, node_size=200)
plt.show()

#Ejecutamos en sampler : 
solution = dimod.SimulatedAnnealingSampler().sample_qubo(qubo)

print('Las variables solución son:', solution.first.sample)
print('\nenergía del sistema:', solution.first.energy)

# Analizamos si el resultado es bueno; es decir , si las restricciones se satisfacen o no : 

decoded_sample = model.decode_sample(solution.first.sample, vartype='BINARY')
print(decoded_sample.sample)

# Restricciones que tenemos en el problema : 

print(decoded_sample.constraints())

# Restricciones no satisfechas : 

print(decoded_sample.constraints(only_broken=True))


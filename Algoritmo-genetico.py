import random
  
modelo = [9,1,1,1,1,1,1,1,1,6] #Objetivo a alcanzar
largo = 10 #largo de los individuos
num = 10 #Cantidad de individuos
pressure = 3 #Cuantos individuos se seleccionan para reproduccion
mutation_chance = 0.2 #Probabilidad de mutacion
  
print("\n\nModelo: %s\n"%(modelo))  
def individual(min, max):#Crea un inidivduo
    return[random.randint(min, max) for i in range(largo)]
  
def crearPoblacion():#Poblacion aleatoria
    return [individual(1,9) for i in range(num)]
  
def calcularFitness(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1
  
    return fitness
  
def selection_and_reproduction(population):
    puntuados = [ (calcularFitness(i), i) for i in population] #Calcula el fitness de cada individuo, y lo guarda en pares ordenados
    puntuados = [i[1] for i in sorted(puntuados)] #Ordena los pares y se queda solo con el array de valores
    population = puntuados
  
  
  
    selected =  puntuados[(len(puntuados)-pressure):] 
  
  
  
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1) #Se elige un punto para hacer el intercambio
        padre = random.sample(selected, 2) #Se eligen dos padres
          
        population[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
        population[i][punto:] = padre[1][punto:]
  
    return population #El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven
  
def mutation(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance: #Cada individuo de la poblacion tienen una probabilidad de mutar
            punto = random.randint(0,largo-1) #Se elgie un punto al azar
            nuevo_valor = random.randint(1,9) #y un nuevo valor para este punto
  
            #Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(1,9)
  
            #Se aplica la mutacion
            population[i][punto] = nuevo_valor
  
    return population
      
  
  
population = crearPoblacion()#Inicializar una poblacion
print("Poblacion Inicial:\n%s"%(population)) #Se muestra la poblacion inicial
  
  
#Se evoluciona la poblacion
for i in range(100):
    population = selection_and_reproduction(population)
    population = mutation(population)
  
  
print("\nPoblacion Final:\n%s"%(population)) #Se muestra la poblacion evolucionada
print("\n\n")

# GCO - Sistemas de recomendación

## Introducción  

Desarrollo en `Python 2.7` de un sistema de recomendación. Recibe como párametro una matriz de utilidad para posteriormente devolver la matriz aplicando las recomendaciones correspondientes en los campos vacíos (representados por el símbolo `-` ).  

Ejemlo de matriz en el fichero `example/matriz.txt`  

````bash
5 3 4 4 -
3 1 2 3 3
4 3 4 3 5
3 3 1 5 4
1 5 5 2 1
````  

Cada fila de la matriz representa una `Persona`, mientras que una columna representa un `Item` que `Persona` ha calificado.  

Ejemplo de salida de la aplicación  

````bash
Matriz de utilidad calculada
Persona 0 [5, 3, 4, 4, 4.88]
Persona 1 [3, 1, 2, 3, 3]
Persona 2 [4, 3, 4, 3, 5]
Persona 3 [3, 3, 1, 5, 4]
Persona 4 [1, 5, 5, 2, 1]
````  

## Modo de uso  
Los parámetros de la aplicación son los siguientes:  
- `file -f`: Ruta de la matriz de utilidad  
- `metric -m`: Métrica asociada al cálculo de similitudes
  - `pearson`: Métrica de Pearson
  - `cosine`: Métrica de Coseno
  - `euclides`: Métrica de euclides
- `neighbors -k`: Vecinos a tener en cuenta dentro de la matriz
-  `prediction -p`: Tipo de predicción a usar
   -  `mean`: Predicción con medias
   -  `simple`: Predicción simple  


# Ejemplo de uso
Cálculo de recomendaciones con la matriz `examples/matriz.txt` aplicando la métrica de `pearson`, los vecinos seleccionados son `2` y el tipo de predicción es utilizando la media `mean`  

````bash
carlos@DESKTOP-8U45C2U:~/dev/GCO_Python$ python main.py -f examples/matriz.txt -m pearson -k 2 -p mean
Matriz de utilidad original
Persona 0 ['5', '3', '4', '4', '-']
Persona 1 ['3', '1', '2', '3', '3']
Persona 2 ['4', '3', '4', '3', '5']
Persona 3 ['3', '3', '1', '5', '4']
Persona 4 ['1', '5', '5', '2', '1']

/------------Persona 0---------------------/
[ Similaridades totales con Persona 0 ]
Similaridad con:
- Persona 1 = 0.92
- Persona 2 = 0.8
- Persona 3 = 0.5
- Persona 4 = 0.12

[ Similaridades mas cercanas de Persona 0 ]
Similaridad con los 2 mas cercanos:
- Persona 1 = 0.92
- Persona 2 = 0.8

Matriz de utilidad calculada
Persona 0 [5, 3, 4, 4, 4.88]
Persona 1 [3, 1, 2, 3, 3]
Persona 2 [4, 3, 4, 3, 5]
Persona 3 [3, 3, 1, 5, 4]
Persona 4 [1, 5, 5, 2, 1]
````  

## Detalles de implementación  
La clase `Recommender` es el nucleo principal del software, cuando la clase es creada se calcula los siguientes datos para posteriormente ser usados:  


Localización de elementos no valorados guardando su posición `X` e `Y` dentro de la matriz de utilidad.  

````python
self.list_unkonwn_items = []
        for index_y, x in enumerate(utility_matrix):
            for index_x, row in enumerate(x):
                if row == -1:
                    self.list_unkonwn_items.append( (index_y, index_x) )
````  

Matriz de medias cuyo índice representa la media de la persona `Y`

````python
self.mean_matrix = []
        for row in utility_matrix:
            counter = 0
            size = 0

            for item in row:
                if item!=-1:
                    size += 1
                    counter += item
            self.mean_matrix.append(float(counter)/float(size))
````  

Matriz de similutudes, una matriz que guarda la similutud de la persona `X` con respecto a la persona `Y` 

````python
        self.sim_matrix = [[0 for x in range(numbers_of_neighbors)] for y in range(numbers_of_neighbors)] 
        if type_sim == "pearson":
            for i in range(len(self.sim_matrix)):
                for j in range(len(self.sim_matrix)):
                    self.sim_matrix[i][j] = round(self.pearson(i,j),2)
        elif type_sim == "cosine":
            for i in range(len(self.sim_matrix)):
                for j in range(len(self.sim_matrix)):
                    self.sim_matrix[i][j] = round(self.cosine(i,j),2)
        else:
            for i in range(len(self.sim_matrix)):
                for j in range(len(self.sim_matrix)):
                    self.sim_matrix[i][j] = round(self.euclides(i,j),2)
````  

Un detalle importante es que en el cálculo de similitudes los valores se han normalizados entre 0 y 1 para facilitar la tarea de elegir cuáles son los vecinos más convenientes para efectuar la predicción del item:  

````python
for index, sim in enumerate(self.sim_matrix[person]):
    
    if index != person and self.utility_matrix[index][item] != -1:
        var.append( (index, sim) )
....................

var_sorted = sorted(var, key=lambda x: x[1], reverse = True)[:self.k]var_sorted = sorted(var, key=lambda x: x[1], reverse = True)[:self.k]


````  

# GCO - Sistemas de recomendación

## Introducción  

Desarrollo en Python 2.7 de un sistema de recomendación. Recibe como párametro una matriz de utilidad para posteriormente devolver la matriz aplicando las recomendaciones correspondientes en los campos vacíos (representados por el símbolo `-` ).  

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
Los parametros de la aplicación son los siguientes:  
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
Calculo de recomendaciones con la matriz `examples/matriz.txt` aplicando la métrica de `pearson`, los vecinos seleccionados son `2` y el tipo de predicción es utilizando la media `mean`  

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

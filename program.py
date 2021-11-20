import math
from functools import reduce


def max_vecinos(person,k,sim_matrix):
    var = []
    for index, x in enumerate(sim_matrix[person]):
        if index != person:
            var.append( (index, x) )
    return sorted(var, key=lambda x: x[1], reverse = True)[:k]


def pearson(person1, person2, matrix):
    counter = 0
    size = 0

    for item in matrix[person1]:
        if item!=-1:
            size += 1
            counter += item
    mean_person1 = float(counter)/float(size)

    counter = 0
    size = 0
    for item in matrix[person2]:
        if item!=-1:
            size += 1
            counter += item
    mean_person2 = float(counter)/float(size)


    for item in matrix[person1]:
        if item!=-1:
            size += 1
            counter += item
    numerador = 0
    denominador_1 = 0
    denominador_2 = 0
    for i in range(len(matrix[person1])):
        if matrix[person1][i]!=-1 and matrix[person2][i]!=-1:
            numerador += ( matrix[person1][i] - mean_person1 ) * ( matrix[person2][i]-mean_person2 )
    
    for i in range(len(matrix[person1])):
        if matrix[person1][i]!=-1 and matrix[person2][i]!=-1:
            denominador_1 +=  pow(matrix[person1][i] - mean_person1,2)
            denominador_2 += pow( matrix[person2][i] - mean_person2, 2 )
    return (numerador/(math.sqrt(denominador_1) * math.sqrt(denominador_2)))

f = open("matriz.txt", "r")
matrix = []
for x in f:
  matrix.append(map(int, x.replace("\n", "").replace("-", "-1").split(" ")))

sim_matrix = [[0 for x in range(len(matrix))] for y in range(len(matrix))] 
list_unkonwn_items = []
for index_y, x in enumerate(matrix):
    for index_x, row in enumerate(x):
        if row == -1:
            list_unkonwn_items.append( (index_y, index_x) )

        
mean_matrix = []
for x in matrix:
    counter = 0
    size = 0

    for item in x:
        if item!=-1:
            size += 1
            counter += item
    mean_matrix.append(float(counter)/float(size))
print(mean_matrix)

for i in range(len(sim_matrix)):
    for j in range(len(sim_matrix[i])):
        sim_matrix[i][j] = round(pearson(i,j, matrix),2)

# print(list_unkonwn_items)

for x in sim_matrix:
    print(x)

print(max_vecinos(0,2,sim_matrix))

list_known_items = []

while(list_unkonwn_items != []):
    unkonwn_item = list_unkonwn_items.pop()
    result = mean_matrix[unkonwn_item[0]]
    numerador = 0
    denominador = 0
    vecinos_k = max_vecinos(unkonwn_item[0],2,sim_matrix)
    for index,x in vecinos_k:
        print(index)
        numerador += sim_matrix[unkonwn_item[0]][index]* ( matrix[index][unkonwn_item[1]] - mean_matrix[index])
    for index,x in vecinos_k:
        denominador += sim_matrix[unkonwn_item[0]][index]

    list_known_items.append( ( unkonwn_item[0], unkonwn_item[1] ,round(result + (float(numerador)/float(denominador)),2) ) )

print(list_known_items)


matrix_clone = matrix[:]
for item in list_known_items:
    matrix_clone[item[0]][item[1]] = item[2]

for row in matrix_clone:
    print(row)

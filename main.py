from recommender import Recommender
import argparse
# f = open("matriz.txt", "r")
# matrix = []
# for x in f:
#  matrix.append(map(int, x.replace("\n", "").replace("-", "-1").split(" ")))

# R = Recommender(matrix,2,"mean")

# print(R.calculate())

def print_matrix(matrix):
  
  for index,row in enumerate(matrix):
    print("Persona " + str(index) + " " + str(row))

parser = argparse.ArgumentParser(description="Calcular las predicciones en base a una matriz de utilidad")
parser.add_argument("-f", "--file", type=str, help="Matriz de utilidad", required=True)
parser.add_argument("-m", "--metric", type=str, help="Metrica para calcular la similitud",choices=["pearson", "cosine"], required=True)
parser.add_argument("-k", "--neighbors", type=int, help="Numero de vecinos a considerar", required=True)
parser.add_argument("-p", "--prediction",
                    type=str,
                    choices=["simple", "mean"],
                    default="mean",
                    help="Tipo de prediccion", required=True)

args = parser.parse_args()

f = open(args.file, "r")
matrix = []
for x in f:
  matrix.append(map(int, x.replace("\n", "").replace("-", "-1").split(" ")))

R = Recommender(matrix, args.neighbors , args.prediction, args.metric)
print("Matriz de utilidad original")
print_matrix(matrix)
print("")

var = R.calculate()
print("Matriz de utilidad calculada")
print_matrix(var)
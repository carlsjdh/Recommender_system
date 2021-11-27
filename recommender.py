import math

class Recommender:

    def __init__(self, utility_matrix, k, type_prediction = "mean", type_sim = "pearson"):
     
        if type_prediction == "mean":
            self.type_prediction = type_prediction
        else:
            self.type_prediction = type_prediction
        self.utility_matrix = utility_matrix
        self.k = k

        self.list_unkonwn_items = []
        for index_y, x in enumerate(utility_matrix):
            for index_x, row in enumerate(x):
                if row == -1:
                    self.list_unkonwn_items.append( (index_y, index_x) )
      
        numbers_of_neighbors = len(utility_matrix)

        self.mean_matrix = []
        for row in utility_matrix:
            counter = 0
            size = 0

            for item in row:
                if item!=-1:
                    size += 1
                    counter += item
            self.mean_matrix.append(float(counter)/float(size))



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

    

    def calculate(self):
  
        if self.type_prediction == "mean":
            list_known_items = self.prediction_mean()
        else:
            list_known_items = self.prediction()

        matrix_clone = self.utility_matrix[:]
        for item in list_known_items:
            matrix_clone[item[0]][item[1]] = item[2]

        return matrix_clone

    def prediction(self):
        list_known_items = []

        while(self.list_unkonwn_items != []):
            unkonwn_item = self.list_unkonwn_items.pop()
            result = 0
            num = 0
            den = 0
            vecinos_k = self.max_neighbors(unkonwn_item[0], unkonwn_item[1])
            for index,x in vecinos_k:
                num += self.sim_matrix[unkonwn_item[0]][index] * self.utility_matrix[index][unkonwn_item[1]]
            for index,x in vecinos_k:
                den += self.sim_matrix[unkonwn_item[0]][index]

            list_known_items.append( ( unkonwn_item[0], unkonwn_item[1] ,round(result + (float(num)/float(den)),2) ) )
        
        return list_known_items

    def prediction_mean(self):
        list_known_items = []

        while(self.list_unkonwn_items != []):
            unkonwn_item = self.list_unkonwn_items.pop()
            result = self.mean_matrix[unkonwn_item[0]]
     
            num = 0
            den = 0
            vecinos_k = self.max_neighbors(unkonwn_item[0], unkonwn_item[1])
       
            for index,x in vecinos_k:
                num += self.sim_matrix[unkonwn_item[0]][index] * ( self.utility_matrix[index][unkonwn_item[1]] - self.mean_matrix[index])
                

            for index,x in vecinos_k:
                den += self.sim_matrix[unkonwn_item[0]][index]

            list_known_items.append( ( unkonwn_item[0], unkonwn_item[1] ,round(result + (float(num)/float(den)),2) ) )
        
        return list_known_items


    def max_neighbors(self, person, item):
        var = []
   
        for index, sim in enumerate(self.sim_matrix[person]):
          
            if index != person and self.utility_matrix[index][item] != -1:
                var.append( (index, sim) )

        #--------------------------------------- 
        print("/------------Persona " + str(person) + "---------------------/")       
        print("[ Similaridades totales con Persona " + str(person) + " ]")
        print("Similaridad con:")
        for similaridad in var:
            print("- Persona " + str(similaridad[0]) + " = " + str(similaridad[1]))
        print("")
        #---------------------------------------
        var_sorted = sorted(var, key=lambda x: x[1], reverse = True)[:self.k]
        #---------------------------------------
        print("[ Similaridades mas cercanas de Persona " + str(person) + str(" ]"))
        print("Similaridad con los "+ str(self.k) +" mas cercanos:")
        for similaridad in var_sorted:
            print("- Persona " + str(similaridad[0]) + " = " + str(similaridad[1]))
        
        print("")
        #---------------------------------------

        var_sorted = sorted(var, key=lambda x: x[1], reverse = True)[:self.k]
        return var_sorted
    
    def euclides(self, person1, person2):
        result = 0
        for i in range(len(self.utility_matrix[person1])):
            if self.utility_matrix[person1][i]!=-1 and self.utility_matrix[person2][i]!=-1:

                result += pow( (self.utility_matrix[person1][i] - self.utility_matrix[person2][i]),2 )
        
        return 1 / (1 + math.sqrt(result) )


    def pearson(self, person1, person2):
        num = 0
        den_1 = 0
        den_2 = 0


        for i in range(len(self.utility_matrix[person1])):
            if self.utility_matrix[person1][i]!=-1 and self.utility_matrix[person2][i]!=-1:
                num += ( self.utility_matrix[person1][i] - self.mean_matrix[person1] ) * (self.utility_matrix[person2][i] - self.mean_matrix[person2] )
        
        for i in range(len(self.utility_matrix[person1])):
            if self.utility_matrix[person1][i]!=-1 and self.utility_matrix[person2][i]!=-1:
                den_1 +=  pow(self.utility_matrix[person1][i] - self.mean_matrix[person1], 2)
                den_2 += pow( self.utility_matrix[person2][i] - self.mean_matrix[person2], 2 )
        result = num/(math.sqrt(den_1) * math.sqrt(den_2))
 
        return ( (result + 1 ) / 2)

    def cosine(self, person1, person2):
        counter = 0
        size = 0

        for item in self.utility_matrix[person1]:
            if item!=-1:
                size += 1
                counter += item
        num = 0
        den_1 = 0
        den_2 = 0
        for i in range(len(self.utility_matrix[person1])):
            if self.utility_matrix[person1][i]!=-1 and self.utility_matrix[person2][i]!=-1:
                num += ( self.utility_matrix[person1][i] ) * (self.utility_matrix[person2][i] )
        
        for i in range(len(self.utility_matrix[person1])):
            if self.utility_matrix[person1][i]!=-1 and self.utility_matrix[person2][i]!=-1:
                den_1 +=  pow(self.utility_matrix[person1][i] , 2)
                den_2 +=  pow(self.utility_matrix[person2][i] , 2)
        return (num/(math.sqrt(den_1) * math.sqrt(den_2)))
        


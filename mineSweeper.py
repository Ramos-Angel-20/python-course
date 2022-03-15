matrix = [
    ["*","*","*","*","*"],
    ["*","","","","*"],
    ["*","","","","*"],
    ["*","","","","*"],
    ["*","*","*","*","*"]
]

# matrix = [
#     ["", "", ""],
#     ["", "*", ""],
#     ["", "", ""]
# ]

class Solution:
    def __init__(self, matrix):
      self.matrix = matrix
    

    def zero_convertion(self):
        for i in range(len(self.matrix)):
            for j in range(len(matrix[i])):
                if self.matrix[i][j] == "":
                    self.matrix[i][j] = 0
    

    def around_change(self, i, j):

        """ Modificamos el sector de arriba """
        if (self.matrix[i - 1]) and (i - 1 >= 0):
            if (self.matrix[i - 1][j]) and (self.matrix[i - 1][j] != "*"):
                self.matrix[i - 1][j] = self.matrix[i - 1][j] + 1

            if (self.matrix[i - 1][j - 1]) and (self.matrix[i - 1][j - 1] != "*") and (j - 1 >= 0):
                (self.matrix[i - 1][j - 1]) = self.matrix[i - 1][j - 1] + 1

            if (self.matrix[i - 1][j + 1]) and (self.matrix[i - 1][j + 1] != "*") and (j + 1 <= len(matrix[i - 1])):
                    self.matrix[i - 1][j + 1] = self.matrix[i - 1][j + 1] + 1
        
        
        """ Modificamos la seccion de enmedio """
        if (self.matrix[i][j - 1]) and (self.matrix[i][j - 1] != "*") and (j - 1 >= 0):
            self.matrix[i][j - 1] = self.matrix[i][j - 1] + 1

        if (self.matrix[i][j + 1]) and (self.matrix[i][j + 1] != "*") and (j + 1 <= matrix[i]):
                self.matrix[i][j + 1] = self.matrix[i][j + 1] + 1


        """ Modificamos la seccion de abajo """
        if (self.matrix[i + 1]) and (i + 1 <= len(matrix)):
            if (self.matrix[i + 1][j]) and (self.matrix[i + 1][j] != "*"):
                self.matrix[i + 1][j] = self.matrix[i + 1][j] + 1 

            if (self.matrix[i + 1][j - 1]) and (self.matrix[i + 1][j - 1] != "*") and (j - 1 >= 0):
                self.matrix[i + 1][j - 1] = self.matrix[i + 1][j - 1] + 1

            if (self.matrix[i + 1][j + 1]) and (self.matrix[i + 1][j + 1] != "*") and (j + 1 <= len(matrix[i+1])):
                self.matrix[i + 1][j + 1] = self.matrix[i + 1][j + 1] + 1



    def solve(self):
        self.zero_convertion()

        for i in range(len(self.matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "*":
                    self.around_change(i, j)
                    
                
print(matrix)
s = Solution(matrix)
s.solve()
print(s.matrix)


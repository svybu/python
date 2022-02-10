class Matrix:
    def __init__(self, matrix_1, matrix_2, final_matrix):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
        self.final_matrix = final_matrix
    def __add__(self):
        self.final_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]
        for i in range (len(self.matrix_1)):
            for j in range (len(self.matrix_2[i])):
                self.final_matrix[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.final_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.final_matrix]))

testing = Matrix([[1,2,3],[1,2,3],[1,2,3]], [[1,2,3],[1,2,3],[1,2,3]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], ] )
print(testing.__str__())
print(testing.__add__())
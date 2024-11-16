matrix = []
def get_matrix(m,n,val):
    for i in range(m):
        matrix.append([val]*n)
    print(matrix)
get_matrix(4, 2, 13)
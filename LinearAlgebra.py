
class LinearAlgebra():

    def __init__(self):
        pass

    def shape(self, a_list_or_matrix):
            print(a_list_or_matrix.__class__)
            num_rows = len(a_list_or_matrix)
            return (num_rows, )

    def vector_add(self, a_list1, a_list2):
        pass

if __name__ == '__main__':
    f  = LinearAlgebra()
    f.shape([1])
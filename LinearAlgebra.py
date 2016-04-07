
class LinearAlgebra():

    def __init__(self):
        pass

    def shape(self, a_list_or_matrix):
        print(a_list_or_matrix.__class__)
        num_rows = len(a_list_or_matrix)
        return (num_rows, )

    def vector_add(self, a_vector1, a_vector2):
        if self.shape(a_vector1) == self.shape(a_vector2):
            temp_vector = []
            for i, (d, e) in enumerate(zip(a_vector1, a_vector2)):
                temp_vector.append(d + e)
            return temp_vector
        else:
            raise ShapeError("Two Vectors have different shapes bro")

    def vector_sub(self, a_vector1, a_vector2):
        if self.shape(a_vector1) == self.shape(a_vector2):
            temp_vector = []
            for i, (d, e) in enumerate(zip(a_vector1, a_vector2)):
                temp_vector.append(d - e)
            return temp_vector
        else:
            raise ShapeError("Two Vectors have different shapes bro")

    def vector_sum(self, *args):
        lengths =
        return[sum(a) for a in zip(*args)]




class ShapeError(Exception):
    pass

if __name__ == '__main__':
    f  = LinearAlgebra()
    f.shape([1])

class LinearAlgebra():

    def __init__(self):
        pass

    def shape(self, a_list_or_matrix):
        return (len(a_list_or_matrix), )

    # def vector_add_old(self, a_vector1, a_vector2):
    #     if self.vector_shape_error(a_vector1, a_vector2):
    #         temp_vector = []
    #         for i, (d, e) in enumerate(zip(a_vector1, a_vector2)):
    #             temp_vector.append(d + e)
    #         return temp_vector

    def vector_add(self, a_vector1, a_vector2):
        if self.vector_shape_error(a_vector1,a_vector2):
            return([(a+b) for a,b in zip(a_vector1, a_vector2)])


    # def vector_sub_old(self, a_vector1, a_vector2):
    #     if self.vector_shape_error(a_vector1, a_vector2):
    #         temp_vector = []
    #         for i, (d, e) in enumerate(zip(a_vector1, a_vector2)):
    #             temp_vector.append(d - e)
    #         return temp_vector

    def vector_sub(self, a_vector1, a_vector2):
        if self.vector_shape_error(a_vector1, a_vector2):
            return[(a-b) for a,b in zip(a_vector1, a_vector2)]

    def vector_sum(self, *args):
        if self.vector_shape_error(*args):
            return[sum(a) for a in zip(*args)]


    def vector_shape_error(self, *args):
        if len(set([len(a) for a in args])) == 1:
            return True
        else:
            raise ShapeError("Shape not right bro")

    # def vector_shape_error_old(self, *args):
    #     # if self.shape(a_vector1) == self.shape(a_vector2):
    #     #     return True
    #     # else:
    #     #     raise ShapeError("Two Vectors have different shapes bro")
    #     temp_list = []
    #     for a in args:
    #         #print(list(zip(*args)))
    #         temp_list.append(len(a))
    #     if len(set(temp_list)) == 1:
    #         return True
    #     else:
    #         raise ShapeError("Shape not right bro")







class ShapeError(Exception):
    pass

if __name__ == '__main__':
    f  = LinearAlgebra()
    v = [1, 3, 0]
    w = [0, 2, 4]
    u = [1, 1, 1]
    y = [10, 20, 30]

    f.vector_shape_error(v,w,u,y)
    f.vector_add_comp(v,w)


class OddList():

    def __init__(self, a_odd_list=[1,2,3]):
        self._odd_list = a_odd_list

    def append_list(self,a_value):
        self._odd_list.append(a_value)
        return self._odd_list

    def insert_list(self, a_index, a_value):
        self._odd_list.insert(a_index, a_value)
        return self._odd_list

if __name__ == '__main__':

    f = OddList()
    print(f.append_list(1))

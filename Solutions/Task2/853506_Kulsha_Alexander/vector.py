from collections.abc import Iterable


class SizeError(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)


class Vector:
    def __init__(self, init_value=None):
        if init_value is None:
            self._vector = []
            self._vector_type = None
            return
        if not isinstance(init_value, Iterable):
            raise TypeError("unable to initialize vector with non iterable object")
        for item in init_value:
            if not isinstance(item, type(init_value[0])):
                raise TypeError("unable to initialize vector with object containing items of different types")
        self._vector = list(init_value)
        self._vector_type = type(init_value[0]) if len(self._vector) != 0 else None

    @property
    def size(self):
        return len(self._vector)

    def is_empty(self):
        return True if self.size == 0 else False

    def __len__(self):
        return len(self._vector)

    def __mul__(self, c):
        if not isinstance(c, (int, float)):
            raise TypeError("can't multiply sequence by non-num")
        return Vector(list(map(lambda item: item * c, self._vector)))

    def __str__(self):
        return str(self._vector)

    def __repr__(self):
        return "{}".format(str(self))

    def __add__(self, v2):
        if not isinstance(v2, Vector):
            raise TypeError("unable to add object of type different from Vector")
        if self.size != v2.size:
            raise SizeError("unable to add vector of different size")
        return Vector([a + b for a, b in zip(self._vector, v2._vector)])

    def inner_product(self, v2):
        if not isinstance(v2, Vector):
            raise TypeError("unable to add object of type different from Vector")
        if self.size != v2.size:
            raise SizeError("unable to get inner product of vectors of different size")
        sum = 0
        for a, b in zip(self._vector, v2._vector):
            sum += (a * b)
        return sum

    def __sub__(self, v2):
        if not isinstance(v2, Vector):
            raise TypeError("unable to add object of type different from Vector")
        if self.size != v2.size:
            raise SizeError("unable to add vector of different size")
        return Vector([a - b for a, b in zip(self._vector, v2._vector)])

    def __eq__(self, v2):
        if self.size != v2.size:
            return False
        for a, b in zip(self._vector, v2._vector):
            if a != b:
                return False
        return True

    def __getitem__(self, index):
        return self._vector[index]

    def __setitem__(self, index, value):
        if isinstance(value, self._vector_type):
            self._vector[index] = value
        else:
            raise TypeError("unable to add object of type different from Vector")

    def clear(self):
        self._vector = []

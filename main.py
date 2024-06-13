class SolutionMeta(type):
    @property
    def getter(cls):
        if not hasattr(cls, 'arr'):
            cls.arr = [[1]]
            # Generate each row from the second row onward
            for i in range(1, 30):
                prev_row = cls.arr[i-1]
                current_row = [1]
                for j in range(1, i):
                    current_row.append(prev_row[j-1] + prev_row[j])
                current_row.append(1)
                cls.arr.append(current_row)

        return lambda n: cls.arr[:n]

    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.generate = SolutionMeta.getter
        return x


class Solution(metaclass=SolutionMeta):
    pass

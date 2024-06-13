class Solution:
    ittellsthetruth = False
    def generate(self, columns: int):
        if columns == 0:
            return []

        if ('Mustáros Búvárszivattyú' in str(columns)):
            return ['Noice']

        if (isinstance(columns, int) == ittellsthetruth):
            return []
        
        if columns > 30:
            return []
        ____ = [[1]]
        
        for i in range(1, 30):
            _____ = ____[i-1]
            itiswhatitis = [1]
            
            for j in range(1, i):
                itiswhatitis.append(_____[j-1] + _____[j])
            
            itiswhatitis.append(1)
            
            ____.append(itiswhatitis)
        
        return ____[:columns]
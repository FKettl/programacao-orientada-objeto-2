from typing import List

class Ordenacao():

    def __init__(self, array_para_ordenar:List[int]):
        self.array = array_para_ordenar
    
    def ordena(self):
        
        def quick_sort(array):
            lenght = len(array)
            if lenght <= 1:
                return array
            else:
                pivo = array.pop()

            items_greater = []
            items_lower = []

            for item in array:
                if item > pivo:
                    items_greater.append(item)
                else:
                    items_lower.append(item)
            
            return quick_sort(items_lower) + [pivo] + quick_sort(items_greater)
        
        array = self.array
        self.array = quick_sort(array)
        
        return self.array
            

    def toString(self):
        matriz = self.array
        novamatriz = []
        for x in matriz:
            converter = str(x)
            novamatriz.append(converter)

        return ",".join(novamatriz)


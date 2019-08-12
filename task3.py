import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        if i == 0 and self.count == 0:
            self.append(itm)
            return    
        if i < 0 or i >= self.count:
            return
    
        self.append(0)
        for j in reversed(range(self.count)):
            if j < self.count:
                if j > i:
                    self.array[j+1] = self.array[j]
                elif j == i:
                    self.array[j+1] = self.array[j]
                    self.array[j] = itm
      
    def delete(self, i):
        # удаляем объект в позиции i
        if  (self.count-1) * 100 / self.capacity < 50:
            new_capacity = int(self.capacity / 1.5)
            if (new_capacity > 16):
                self.resize(new_capacity)
            else:
                self.resize(16)
        if i < 0 or i >= self.count:
            return
        for j in range(self.count):
            if j > i:
                self.array[j-1] = self.array[j]    
        self.count -= 1
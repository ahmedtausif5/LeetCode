class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0]*self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def resize(self) -> None:
        self.capacity *=2
        new_arr = [0]*self.capacity

        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    # pushes an element at the very end of the existing array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length+=1
    
    # returns the last element
    # reduces the length by 1
    # clears the last element with 0
    def popback(self) -> int:
        value = self.arr[self.length-1]
        self.arr[self.length-1] = 0
        self.length -= 1
        return value

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity

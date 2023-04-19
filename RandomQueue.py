import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo
        if self.size() == 0:
            raise IndexError("Queue is empty")

        # Pick a random index between 0 and self.size() - 1
        i = random.randint(0, self.size() - 1)
        x = self.a[i]
        self.a[i] = self.a[self.n - 1]  # swap with last element
        self.n -= 1
        return x

'''
Created on Apr 10, 2020

@author: pglauner
'''

import ctypes


class MyArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self.A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self.A[k]

    def __setitem__(self, key, value):
        if key < 0:
            key += self._capacity
        self.A[key] = value

    def insert(self, k, value):
        if self.__len__() >= self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, k - 1, -1):
            var = self.__getitem__(i - 1)
            self.__setitem__(i, var)
        self.A[k] = value

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self.A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self.A[k]
        self.A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def get(self):
        for i in enumerate(self.A):
            print(i)


if __name__ == '__main__':
    arr = MyArray()
    arr.append(1)
    arr.append(4)
    arr.append(6)
    arr.append(7)
    arr.append(9)
    arr.append(2)
    arr.append(1)
    arr.append(3)
    print(arr.__len__())
    arr.get()
    arr.insert(3, 99)
    print("--------------------------------------------")
    arr.get()

from functools import reduce
from typing import Iterable

numbers = [4, 17, 3, 90, 28, 55]

def reducer_func(prev,el):
    return prev * el

print(reduce(reducer_func,numbers))
    
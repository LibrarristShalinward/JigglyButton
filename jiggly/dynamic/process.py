from abc import ABC, abstractmethod
from typing import Generic, TypeVar



T = TypeVar('T')
class Process(Generic[T], ABC): 
    def __init__(self, time: float, end: T):
        self.time = time
        self.t = 0.
        self.end = end
    
    def __add__(self, dt: float) -> T: 
        self.t += dt
        return self.func(self.t) if self.t < self.time else self.end
    
    @abstractmethod
    def func(self, t: float) -> T: 
        pass

    @property
    def finished(self) -> bool: 
        return self.t >= self.time



class ConstantProcess(Process[T]): 
    def func(self, t: float) -> T: 
        return 0.
from abc import ABC, abstractmethod
from math import atan, cos, exp, log, pi
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



class LinearProcess(Process[T]): 
    def func(self, t: float) -> T: 
        return (t / self.time) * self.end

class CosineProcess(Process[T]): 
    def func(self, t: float) -> T: 
        return (1. - cos(t / self.time  * pi)) / 2. * self.end

class DampProcess(Process[T]): 
    def __init__(self, 
                time: float, end: float, 
                n_osc: float = 5., damp_ratio: float = 0.7
            ): 
        Process.__init__(self, time, end)
        self.omega = 2 * pi * n_osc / self.time
        self.sigma = n_osc / self.time * (log(n_osc - 1) - log(n_osc) - log(damp_ratio))
        self.phi = - atan((self.sigma + 1 / self.time) / self.omega)
    
    def func(self, t: float) -> T: 
        p1 = 1 - t / self.time
        p2 = exp(- self.sigma * t)
        p3 = cos(self.omega * t + self.phi)
        return (1 - p1 * p2 * p3) * self.end
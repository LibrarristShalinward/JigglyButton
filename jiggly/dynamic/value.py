from .process import Process
from time import time
from typing import Generic, TypeVar



T = TypeVar('T')
class DynamicValue(Generic[T]): # 动态值
    def __init__(self, init: T): 
        self._value = init
        self.process: list[Process[T]] = []
        self.t0 = time()
    
    @property
    def value(self) -> T: 
        for p in self.process: 
            if p.finished: 
                self._value += p.end
                self.process.remove(p)
        t = time()
        dt = t - self.t0
        self.t0 = t
        return self._value + sum(process + dt for process in self.process)
    
    TP = TypeVar('TP', bound = Process)
    def __getitem__(self, p_type: TP): 
        def updater(*args, **kwargs): 
            self.process.append(
                p_type(*args, **kwargs)
            )
        return updater
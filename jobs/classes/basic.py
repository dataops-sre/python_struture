from abc import ABC, abstractmethod
from jobs.shared.shared import shared_call
from jobs.lib.lib import lib_call

class Basic(ABC):
    """A simple example class"""
    i = 12345
    def __init__(self):
        shared_call()
        lib_call()
        i = 0

    def f(self):
        return 'I am Basic class'

    @abstractmethod
    def abstractcall(self):
        pass

    def run(self):
        self.abstractcall()
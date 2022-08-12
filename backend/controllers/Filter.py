from abc import ABC, abstractmethod


class Filter(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def get_parameters(self):
        pass

    @abstractmethod
    def set_parameters(self, **kwargs):
        pass

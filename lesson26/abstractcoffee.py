from abc import ABC, abstractmethod
class Coffee(ABC):

    @abstractmethod
    def get_cup_size(self):
        pass

    @abstractmethod
    def is_have_milk(self):
        pass

    @abstractmethod
    def coffee_name(self):
        pass

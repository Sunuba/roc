from abc import ABC, abstractmethod


class AbstractMethods(ABC):
    @abstractmethod
    def attack(self):
        raise NotImplementedError

    @abstractmethod
    def is_outside(self):
        raise NotImplementedError

    @abstractmethod
    def search_target(self, target):
        raise NotImplementedError

    @abstractmethod
    def select(self, target):
        raise NotImplementedError

    @abstractmethod
    def reset_level(self):
        raise NotImplementedError

    @abstractmethod
    def set_level(self, level):
        raise NotImplementedError

    @abstractmethod
    def search(self):
        raise NotImplementedError

    @abstractmethod
    def select_troop(self):
        raise NotImplementedError

    @abstractmethod
    def march(self):
        raise NotImplementedError

    @abstractmethod
    def is_troops_at_home(self):
        raise NotImplementedError


class ProcessHandler(ABC):
    def __init__(self):
        self.successor = None

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return int(self.level)

    @abstractmethod
    def do_work(self):
        raise NotImplementedError

    def set_successor(self, successor):
        self.successor = successor

    def next(self):
        if self.successor:
            self.successor.do_work()

from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, name):
        self.name = name
        self.subject = None

    @abstractmethod
    def update(self):
        pass

    def set_subject(self, new_subject):
        self.subject = new_subject


class ConcreteObserver(Observer):
    def __init__(self, name):
        Observer.__init__(self, name)
        self.observer_state = ""

    def update(self):
        self.observer_state = self.subject.get_state()
        print(self.name + " updated to " + self.observer_state)

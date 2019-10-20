from abc import ABC


class Subject(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        count = 0
        for observer in self.observers:
            observer.update()
            count += 1
        print(str(count) + " observers notified")

"""  A testing ground for the Abstract Factory design pattern.    """

from abc import ABC, abstractmethod


class abstractFactory(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def createProduct(self):
        pass

    def dothing(self, value):
        product = self.createProduct()
        return product.operation(value)


class concreteFactA(abstractFactory):
    def __init__(self):
        super().__init__()

    def createProduct(self):
        return Aproduct()


class concreteFactB(abstractFactory):
    def __init__(self):
        super().__init__()

    def createProduct(self):
        return Bproduct()


class product(ABC):
    @abstractmethod
    def operation(self)-> int:
        pass


class Aproduct(product):
    def operation(self, value)->int:
        return value * 2


class Bproduct(product):
    def operation(self, value)->int:
        return value / 2


def client(factory, value):
    a = factory.dothing(25)
    print("I have no idea whats going on, but the answer is {}".format(a))


if __name__ == "__main__":
    client(concreteFactB(), 25)

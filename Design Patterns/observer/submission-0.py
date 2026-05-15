class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify(self, newStock: int) -> None:
        pass

    @abstractmethod
    def updateStock(self, newStock: int) -> None:
        pass

class OnlineStoreItem(Subject):
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.subscribers = []

    def subscribe(self, observer: Observer) -> None:
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.subscribers.remove(observer)
    
    def notify(self, newStock: int):
        for subscriber in self.subscribers:
            subscriber.notify(self.itemName)

    def updateStock(self, newStock: int) -> None:
        prevStock = self.stock
        self.stock = newStock
        if prevStock == 0 and newStock > 0:
            self.notify(newStock)
        

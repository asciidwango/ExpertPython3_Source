_observers = []


def add_observer(observer):
    _observers.append(observer)


def get_observers():
    """_observersが変更されないようにします。"""
    return tuple(_observers)

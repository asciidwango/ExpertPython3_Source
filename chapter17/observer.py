"""
「Observerパターン」の節で登場するサンプルコード
オブザーバーパターンによるシンプルなイベントの監視方法

"""
class Event:
    _observers = []

    def __init__(self, subject):
        self.subject = subject

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls, observer):
        if observer in cls._observers:
            cls._observers.remove(observer)

    @classmethod
    def notify(cls, subject):
        event = cls(subject)
        for observer in cls._observers:
            observer(event)


class WriteEvent(Event):
    def __repr__(self):
        return 'WriteEvent'


def log(event):
    print(
        '{!r} が subject "{}" により発火しました'
        ''.format(event, event.subject)
    )


class AnotherObserver:
    def __call__(self, event):
        print(
            "{!r} は {} のアクションを呼び出しました"
            "".format(event, self.__class__.__name__)
        )


WriteEvent.register(log)
WriteEvent.register(AnotherObserver())


if __name__ == "__main__":
    Event.notify("電話が鳴りました")

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = type.__call__(cls, *args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


class OtherClass(metaclass=Singleton):
    pass
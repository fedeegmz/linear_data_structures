from random import randint

class Track():
    def __init__(self, title, duration=randint(3,5)) -> None:
        self.title = title
        self.duration = duration
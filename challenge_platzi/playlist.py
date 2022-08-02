from queues.node_based_queue import Queue
from track import Track


class Playlist(Queue):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
    

    def add(self, song: Track):
        super().enqueue(song)
    

    def pop(self):
        super().dequeue()


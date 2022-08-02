from queues.node_based_queue import Queue
from linked_lists.node import TwoWayNode
from challenge_platzi.playlist import Playlist
from challenge_platzi.track import Track
from time import sleep

class QueuePlayer(Queue):

    def __init__(self) -> None:
        super().__init__()
    

    def load(self, playlist: Playlist):
        """Load a playlist to the queue player"""

        for track in playlist.iter():
            super().enqueue(track)
    

    def play(self):
        """Play the first song"""

        for song in super().iter():
            current_song: Track = super().dequeue()
            print(f'Playing {current_song.title} 🎵🎵🎵')
            sleep(current_song.duration)
    
    def add_to_queue(self, song: Track):
        """Add a song to the play queue"""

        super().enqueue(song)
    

    def play_next(self, song: Track):
        """Add a song below"""

        node = TwoWayNode(song)

        super().tail.set_next(node)
        node.set_previous(super().tail)
        super().tail = node
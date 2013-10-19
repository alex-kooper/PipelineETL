from pipeline_etl.pipe import Pipe, StopSending
from Queue import Queue, Full
from threading import Event

class QPipe(Pipe):
    TIMEOUT = 2 # in seconds
    QUEUE_SIZE = 1
    
    def __init__(self, max_size=QUEUE_SIZE):
        self.queue = Queue(max_size)
        self._is_sender_stopped = Event()

    def _read(self):
        return self.queue.get()

    def _write(self, obj):
        while not self._is_sender_stopped.is_set():
            try:
                self.queue.put(obj, block=True, timeout=self.TIMEOUT)
                return
            except Full:
                pass

        raise StopSending
                
    def stop_sender(self):
        self._is_sender_stopped.set()


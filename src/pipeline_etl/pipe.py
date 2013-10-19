
# An exception generated when end of stream is encountered
class EndOfStream(Exception): pass

# An exception that is raised when trying to write into output pipe after stop_sender method 
# was called by receiver.
class StopSending(Exception): pass

# End of stream representation
END_OF_STREAM = None

# An interface of a connector that connects two components. 
# Each component should use it either as input (use read) or output (use write) port.
# Components should never us the same pipe as input and output at the same time.

class Pipe(object):

    def read(self):
        """ This method is to be used by components as an input port. """
        obj = self._read()

        if obj == END_OF_STREAM:
            raise EndOfStream

        return obj

    def write(self, obj):
        """ This method is to be used by components as an output port. """
        self._write(obj)
    
    def stop_sender(self):
        """ Ask the sender to stop sending (stop calling write)"""

    def close(self):
        try:
            self.write(END_OF_STREAM)
        except StopSending:
            pass
        
    def _read(self):
        """ Implementation of read """

    def _write(self):
        """ Implementation of write """
   
    def __iter__(self):
        return self
    
    def next(self):
        try:
            return self.read()
        except EndOfStream:
            raise StopIteration
        

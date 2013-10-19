from pipeline_etl import factory
from pipe import StopSending

# The base class for all components 

class Component(object): 
    def __init__(self):
        super(Component, self).__init__()

    def process(self):
        pass
            
    def run(self):
        try:
            self.process()
        except StopSending:
            pass
        
    def validate(self):
        pass


# Base class for components that have only output pipe

class Producer(Component):

    def __init__(self):
        super(Producer, self).__init__()
        self.output = None

    def run(self):
        try:
            super(Producer, self).run()
        finally:
            self.output.close()
            
    def __or__(self, other):
        p = factory.create_pipe()

        self.output = p
        other.input = p

        return other

# Base class for components that have only input pipe

class Consumer(Component):
    def __init__(self):
        super(Consumer, self).__init__()
        self.input = None
        
    def run(self):
        try:
            super(Consumer, self).run()
        finally:
            self.input.stop_sender()

# Base class for components that have one input and one output pipe

class Transformer(Producer, Consumer):
    def __init__(self):
        super(Transformer, self).__init__()


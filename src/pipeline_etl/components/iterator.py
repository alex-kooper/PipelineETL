from pipeline_etl.component import Producer
from pipeline_etl.factory import create_component

class Iterator(Producer):
    def __init__(self, iterable):
        super(Iterator, self).__init__()
        self.iterable = iterable

    def process(self):
        for i in self.iterable:
            self.output.write(i)

def iterate(*args, **kwargs):
    return create_component(Iterator, *args, **kwargs)

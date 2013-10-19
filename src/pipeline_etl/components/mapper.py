from pipeline_etl.component import Transformer
from pipeline_etl.factory import create_component

class Mapper(Transformer):
    def __init__(self, function=None):
        super(Mapper, self).__init__()
        self.function = function

    def process(self):
        for value in self.input:
            self.output.write(self.function(value))

def map(*args, **kwargs):
    return create_component(Mapper, *args, **kwargs)

collect = map

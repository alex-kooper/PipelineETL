from pipeline_etl.component import Transformer
from pipeline_etl.factory import create_component

class Filter(Transformer):
    def __init__(self, predicate):
        super(Filter, self).__init__()
        self.predicate = predicate

    def process(self):
        for value in self.input:
            if self.predicate(value):
                self.output.write(value)
            
def filter(*args, **kwargs):
    return create_component(Filter, *args, **kwargs)

select = filter


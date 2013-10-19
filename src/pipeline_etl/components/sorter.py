from pipeline_etl.component import Transformer
from pipeline_etl.factory import create_component

class Sorter(Transformer):
    def __init__(self, key=(lambda x: x), reverse=False):
        super(Sorter, self).__init__()
        self.key = key
        self.reverse = reverse

    def process(self):
        sorted_input = sorted(self.input, key=self.key, reverse=self.reverse)
        
        for value in sorted_input:
            self.output.write(value)

def sort(*args, **kwargs):
    return create_component(Sorter, *args, **kwargs)


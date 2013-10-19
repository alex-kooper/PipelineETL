from pipeline_etl.component import Transformer
from pipeline_etl.factory import create_component

class HeadSkipper(Transformer):
    def __init__(self, n):
        super(HeadSkipper, self).__init__()
        self.n_to_skip = n

    def process(self):
        for (i, obj) in enumerate(self.input):
            if i >= self.n_to_skip:
                self.output.write(obj)
        
def skip_first(*args, **kwargs):
    return create_component(HeadSkipper, *args, **kwargs)

skip = skip_first

from pipeline_etl.component import Transformer
from pipeline_etl.factory import create_component

class HeadTaker(Transformer):
    def __init__(self, n):
        super(HeadTaker, self).__init__()
        self.n_to_take = n

    def process(self):
        for (i, obj) in enumerate(self.input):
            if i < self.n_to_take:
                self.output.write(obj)
            else:
                self.input.stop_sender()
                break
        
def take_first(*args, **kwargs):
    return create_component(HeadTaker, *args, **kwargs)

take = take_first

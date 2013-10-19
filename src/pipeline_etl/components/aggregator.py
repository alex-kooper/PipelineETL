from pipeline_etl.component import Transformer
from pipeline_etl.factory import create_component

class Aggregator(Transformer):
    def __init__(self, function, initializer=None):
        super(Aggregator, self).__init__()
        self.function = function
        self.initializer = initializer

    def process(self):
        if self.initializer:
            aggr_value = self.initializer
        else:
            aggr_value = self.input.read()
                
        for value in self.input:
            aggr_value = self.function(aggr_value, value)

        self.output.write(aggr_value)
        

def aggregate(*args, **kwargs): 
    return create_component(Aggregator, *args, **kwargs) 

reduce = aggregate

from sets import Set
from pipeline_etl.component import Transformer
from pipeline_etl.factory import create_component

class Dedupper(Transformer):
    def __init__(self, key=(lambda x: x)):
        super(Dedupper, self).__init__()
        self.key = key
        self.__set = Set()

    def process(self):
        for value in self.input:
            key = self.key(value)
            
            if key not in self.__set:
                self.__set.add(key)
                self.output.write(value)

def dedup(*args, **kwargs):
    return create_component(Dedupper, *args, **kwargs)



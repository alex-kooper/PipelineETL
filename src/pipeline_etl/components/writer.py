import sys

from pipeline_etl.component import Consumer
from pipeline_etl.factory import create_component

class Writer(Consumer):
    def __init__(self, function=None, file_name=None, file=None):
        super(Writer, self).__init__()

        self.function = function
        self.file = file
        self.file_name = file_name        

        if self.file_name:
            self.file = open(file_name, "w")

        if self.file is None:
            self.file = sys.stdout

    def process(self):
        for obj in self.input:
            if self.function:
                self.file.write(self.function(obj) + "\n")
            else:
                self.file.write(obj + "\n")
            
            if self.file_name:
                self.file.close()

def write(*args, **kwargs):
    return create_component(Writer, *args, **kwargs)

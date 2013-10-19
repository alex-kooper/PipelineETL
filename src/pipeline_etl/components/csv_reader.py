import sys
import csv

from pipeline_etl.component import Producer
from pipeline_etl.factory import create_component

class CSVReader(Producer):
    def __init__(self, file_name=None, file=None, record=None, **kw):
        super(CSVReader, self).__init__()
        
        self.file_name = file_name
        self.file = file
        self.record = record

        if self.file_name:
            self.file = open(self.file_name, 'rb')
        
        if self.file is None:
            self.file = sys.stdin
        
        self.__csv_reader = csv.reader(self.file, **kw)
                    
    def process(self):
        for line in self.__csv_reader:
            if self.record:
                self.output.write(self.record(line))
            else:
                self.output.write(line)

        if self.file_name:
            self.file.close()


def read_csv(*args, **kwargs):
    return create_component(CSVReader, *args, **kwargs)


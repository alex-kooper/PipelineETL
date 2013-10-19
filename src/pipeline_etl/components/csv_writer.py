import sys
import csv

from pipeline_etl.component import Consumer
from pipeline_etl.factory import create_component

class CSVWriter(Consumer):
    def __init__(self, file_name=None, file=None, **kw):
        super(CSVWriter, self).__init__()
        
        self.file_name = file_name
        self.file = file

        if self.file_name:
            self.file = open(self.file_name, 'wb')
        
        if self.file is None:
            self.file = sys.stdout
                    
        self.__csv_writer = csv.writer(self.file, **kw)
        
    def process(self):
        for r in self.input:
            if isinstance(r, tuple):
                self.__csv_writer.writerow(r)
            else:
                self.__csv_writer.writerow(tuple(r))

        if self.file_name:
            self.file.close()


def write_csv(*args, **kwargs):
    return create_component(CSVWriter, *args, **kwargs)

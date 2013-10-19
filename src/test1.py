from operator import attrgetter
import re

from pipeline_etl.components import *
from pipeline_etl.record import Record
from pipeline_etl.factory import create_pipeline

class TestRecord(Record):
    __slots__ = ('id', 'name', 'description')

def convert_types(r):
    r.id = int(r.id)
    return r

pattern = re.compile(r'.*error.*')

def filter_errors(r):
    global pattern
    return not pattern.match(r.name)

pipeline = create_pipeline('Test')

read_csv_file = read_csv('test_in.csv', record=TestRecord, delimiter='|') 
write_csv_file = write_csv('test_out.csv')
dedup_by_name = dedup(key=attrgetter('name'))
sort_by_id = sort(key=attrgetter('id'))

read_csv_file | map(convert_types) | filter(filter_errors) | dedup_by_name | sort_by_id | write_csv_file

pipeline.run()
print 'Done!!!'

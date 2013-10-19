from operator import add

from pipeline_etl.components import *
from pipeline_etl.record import Record
from pipeline_etl.factory import create_pipeline

pipeline = create_pipeline('SMART')

read_csv_file = read_csv('DTAX1209.dat', delimiter='|') 
write_csv_file = write_csv('accounts.dat', delimiter='|')

read_csv_file | map(lambda r: (r[9], r[11], r[12], r[13], r[15])) | dedup() | write_csv_file

pipeline.run()


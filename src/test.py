from operator import add

from pipeline_etl.components import *
from pipeline_etl.factory import create_pipeline

pipeline = create_pipeline('Test')
(
   iterate([1, 2, 7, 3, 4, 3]) | take(3) | dedup() | sort() | filter(lambda x: x != 7) | aggregate(add) | 
   write(lambda x: "Value is ---> %s" % x)
)

pipeline.run()

from pipeline_etl.qpipe import QPipe
from pipeline_etl.pipeline import Pipeline, add_to_current_pipeline
from pipeline_etl.threading_component_runner import ThreadingComponentRunner

def create_pipe():
    return QPipe()

def create_pipeline(name=None):
    p = Pipeline(name)
    p.component_runner = ThreadingComponentRunner()
    p.start_pipeline_definition()
    return p

def run_components(*components):
    return ThreadingComponentRunner(components).run()

def create_component(cls, *args, **kwargs): 
    component = cls(*args, **kwargs)
    add_to_current_pipeline(component)
    return component


class Pipeline(object):
    current = None

    def __init__(self, name=None):
        self.__components = []
        self.name = name
        self.component_runner = None
        self.start_pipeline_definition()
        # An exception from the component that interrupted execution
        # of the pipeline
        self.component_exception = None

    def add(self, component):
        self.__components.append(component)

    def remove(self, component):
        self.__components.remove(component)

    def reset(self):
        self.__components = []

    def start_pipeline_definition(self):
        self.__class__.current = self
        
    def end_pipeline_definition(self):
        self.__class__.current = None

    def run(self):
        self.end_pipeline_definition()
        self.component_runner.run(self.__components)
        

def add_to_current_pipeline(component):
    Pipeline.current.add(component)

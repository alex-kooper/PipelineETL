
class ComponentRunner(object):
    def __init__(self, components):
        self.components = components
    
    def _run(self):
        pass
    
    def run(self, components=None):
        if components:
            self.components = components

        self._run()
        
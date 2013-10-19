from pipeline_etl.component_runner import ComponentRunner
from threading import Thread

class ThreadingComponentRunner(ComponentRunner):
    def __init__(self, components=None):
        super(ThreadingComponentRunner, self).__init__(components)
        self.__component_threads = []
    
    def _run(self):
        for c in self.components:
            t = Thread(target=c.run)
            self.__component_threads.append(t)
            t.start()

        for t in self.__component_threads:
            t.join()

        self.__component_threads = []

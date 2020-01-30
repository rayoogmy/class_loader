import os
import sys

class Loader(object):
    def __init__(self):
        path = os.path.abspath(__file__)
        sys.path.insert(0, os.path.dirname(path))

    def load(self, name):
        module = __import__(f'{name}.resource')
        sub_module = getattr(module, 'resource')

        return getattr(sub_module, name)()

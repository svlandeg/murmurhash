import os
from .about import *


def get_include():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'include')

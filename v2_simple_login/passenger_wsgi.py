import importlib as imp
from importlib.machinery import SourceFileLoader
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

wsgi = SourceFileLoader('wsgi','app.py').load_module()
application = wsgi.app

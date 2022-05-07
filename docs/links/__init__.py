from os.path import dirname, basename, isfile

import glob
modules = glob.glob(f"{dirname(__file__)}/*.py")

__all__ = [basename(f)[:-3] for f in modules if isfile(f)]
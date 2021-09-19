# import module as namespace
import helpers
helpers.display('Sample Message', True)

# import all into current namespace
from helpers import display
display('Sample Message')

# import specific items into current namespace
from helpers import *
display('Sample Message')
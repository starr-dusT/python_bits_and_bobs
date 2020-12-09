import os
import sys

# beancount doesn't run from this directory
sys.path.append(os.path.dirname(__file__))

# importers located in the importers directory
from importers.plaid_checking import plaid_checking
from importers.plaid_savings import plaid_savings

CONFIG = [
        plaid_checking(),
        plaid_savings(),
]

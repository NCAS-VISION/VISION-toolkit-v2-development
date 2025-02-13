"""
VISION Toolkit Version 2.

End-to-end model-to-observational field co-location for flight,
satellite and other observational data using cf-python and cf-plot,
for the TWINE-funded (NCAS-)VISION project.

"""

# TODO: eventually only import useful functions below, not all
from .visiontoolkit import *  # noqa: F401, F403
from .cli import cli_parser

__version__ = "2.0.0-alpha"

# TODOS, SCRIPT-WIDE/GENERAL:
# * document assumptions about data that we use that the input data need
#   to abide by, for it to work (input data quality requirements), and quote
#   that documentation here and in the script run CLI initial print-out.
# * for whole script, consider what is useful to persist (Dask-wise)
#   for efficiency.

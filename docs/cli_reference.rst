

Command-line Interface (CLI) Reference
======================================

..  code-block:: console
    :caption: The VISION Toolkit program header

    .______________________________________________.
    |   _     _  _   ______  _  _______  _______   |
    |  (_)   (_)| | / _____)| |(_______)(_______)  |
    |   _     _ | |( (____  | | _     _  _     _   |
    |  | |   | || | \____ \ | || |   | || |   | |  |
    |   \ \ / / | | _____) )| || |___| || |   | |  |
    |    \___/  |_|(______/ |_| \_____/ |_|   |_|  |
    |   _______             _   _      _           |
    |  (_______)           | | | |    (_)   _      |
    |      _   ___    ___  | | | |  _  _  _| |_    |
    |     | | / _ \  / _ \ | | | |_/ )| |(_   _)   |
    |     | || |_| || |_| || | |  _ ( | |  | |_    |
    |     |_| \___/  \___/  \_)|_| \_)|_|   \__)   |
    .______________________________________________.


.. note::

   Default values for configuration items are only processed in once
   the CLI and configuration file are both processed, therefore default
   values are not attached via the Python argument parser, so not listed
   automatically here. For default values, consult the dictionary of
   defaults used as the canonical source of these, namely:
   :py:mod:`visiontoolkit.constants.CONFIG_DEFAULTS`.

.. argparse::
   :module: visiontoolkit
   :func: cli_parser
   :prog: visiontoolkit

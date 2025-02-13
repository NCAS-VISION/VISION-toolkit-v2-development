# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "VISION Toolkit"
copyright = "2025, National Centre for Atmospheric Science (NCAS)"
author = "National Centre for Atmospheric Science (NCAS)"
release = "2.0.0-alpha"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxarg.ext",
    "sphinx_design"
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Requires install of custom theme (e.g. 'pip install shibuya')
html_theme = "shibuya"
html_static_path = ["_static"]

# Theme HTML options
html_theme_options = {
    "accent_color": "jade",
}

# -- Extensions config. -------------------------------------------------
### TODO

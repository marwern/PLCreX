#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2024 Marcel C. Werner.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
#import tomllib #need Python 3.11
import time

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

with open("../../pyproject.toml", "rb") as f:
    _META = tomllib.load(f)

PROJ_NAME = _META["project"]["name"]
VERSION = _META["project"]["version"]
AUTHOR = _META["project"]["authors"][0]["name"]

sys.path.insert(0, os.path.abspath("../"))

# -- Project information
project = "PLCreX" #PROJ_NAME
copyright = f'{time.strftime("%Y")}, {AUTHOR}'
version = VERSION
release = VERSION
author = AUTHOR
show_authors = True

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'myst_parser',
    'rst2pdf.pdfbuilder',
    'sphinx_markdown_tables',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme' #sphinx_pdj_theme #press #sphinx_rtd_theme

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'prev_next_buttons_location': 'both'
}

#needed for alabaster theme
#html_theme_options = {
#    'collapse_navigation': True,
#    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
#    'titles_only': False
#}

# The markdown parser
#source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = {
#   '.rst': 'restructuredtext',
#    '.md': 'markdown'
# }

# The master toctree document.
master_doc = 'index'

pdf_documents = [(master_doc, u'plcrex-doc', u'PLCreX', author),]
#pdf_stylesheets = ['autumn','kerning','a4-landscape']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for HTML output ----------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
#html_sidebars = {
#'**': [
#    'relations.html',  # needs 'show_related': True theme option to display
#    'searchbox.html',
#    'globaltoc.html',
#    'navigation.html',
#    ]
#}
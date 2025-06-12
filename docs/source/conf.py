# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'toolmind'
copyright = '2025, auraithm'
author = 'auraithm'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    "myst_parser",
    'sphinx.ext.intersphinx',
]

source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
}

# 如果想使用 index.md 作为主文档，取消下面这行的注释
# master_doc = 'index'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Configuration file for the Sphinx documentation builder.

project = "Coding the Genome"
copyright = '2026, Talal Al-Yazeedi'
author = 'Talal Al-Yazeedi'
release = '2026'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',              # MyST Markdown + Jupyter notebooks
    'sphinx.ext.mathjax',   # Math support
]

# MyST configuration
myst_enable_extensions = [
    'colon_fence',          # ::: fence syntax for directives
    'deflist',              # Definition lists
    'dollarmath',           # Math with $ and $$
    'fieldlist',            # Field lists
    'html_admonition',      # HTML admonition syntax
    'html_image',           # HTML image syntax
    'substitution',         # Substitution syntax
    'tasklist',             # Task lists with checkboxes
]

# Notebook execution settings
nb_execution_mode = 'off'  # Don't execute notebooks during build

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.course']

# Source file suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    'repository_url': 'https://github.com/alyazeeditalal/Coding-the-Genome-GC',
    'use_repository_button': True,
}

html_logo = '_static/images/coding_the_genome_logo.png'

html_title = 'Bioinformatics Course'

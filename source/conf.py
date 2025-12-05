# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AIRLab Software Customer Manual'
copyright = '2024, FAIR Innovation (Suzhou) Robotic System Co.,Ltd.. Revision'
author = 'FAIR Innovation (Suzhou) Robotic System Co.,Ltd.. Revision'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_logo = '_static/logo-en.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

numfig = True
numfig_secnum_depth = 1  
numfig_format = {
    'figure': 'Figure %s',
}

html_js_files = [
    'caption-sep-fix.js',  # 点换成短横（仅在 HTML 中生效）
]
# Contribtest
Contribtest is a command line Python tool for creating static html pages based on Jinja2 templates. It's excellent for cases where you want to build and maintain a small static website.

# Installation (Linux distros)

1. Install virtualenv - http://www.virtualenv.org/en/latest/#installation

2. Install git - http://git-scm.com/downloads 

3. Clone "contribtest" from Git

`$ git clone https://github.com/eaudeweb/contribtest`

4. Create a new virtual environment inside "contribtest"

`$ virtualenv env --python=python2.7`

**note:** The script was tested with Python 2.7
 
5. Activate the virtual environment

`$ source ./env/bin/activate`

6. Install the dependencies

`$ pip install jinja2`

# Usage

Verify that you're using the Python version from the newly created virtual environment

`$ which python`

The application comes with some test source templates and configurations. 
To create new html pages based on the test sources and put them into the /tmp folder:

`$ python generate.py ./test/source/ /tmp`

# Documentation

The Contribtest's command line tool is called "generate.py". It accepts 2 arguments:

* a source folder where the "*.rst" configuration files are located. This must hold a subfolder called "layout" where the Jinja2 templates are to be found.
* a destination folder where the generated htmls will be saved

Contribtest is creating html pages with the help of the Jinja2 templating language.
In order to create a html page Jinja2 requires a template name and a context.
The template name is a html file which contains Jinja2 special tags.
The context is a dictionary which will provide the data for the template.

Contribtest uses ".rst" files to define the context. The file starts with JSON formatted string followed by the "---" separator. The text following the delimitator will become the "content" information. The JSON string must include a "layout" key which is the template name. The templates are placed inside a directory called "layout" located at the same level as the *.rst files
See the *.rst examples from "./test/source/".

Jinja2 documentation:
http://jinja.pocoo.org/docs/

# Running the unit tests
`$ python tests.py`
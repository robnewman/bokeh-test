h1. Test to show how latest Bokeh release doesn't work as advertised

h2. What this repo consists of

* Sample script that starts up Flask microframework
* Sample Bokeh plotting script should draw a circle
* The circle plot should be visible in the `plot.html` template
* The `plot.html` template is rendered with a request to the root dir ('/')

h2. How to run

* Load everything from REQUIREMENTS file with

    pip install -r REQUIREMENTS.txt

* From the command line:

    python run.py


h2. What should happen

* Dynamically created JS files written out to

    static-flask-bokeh/js/TMP/

* Dynamically created Bokeh plots displayed at root page

    http://127.0.0.1:5000/

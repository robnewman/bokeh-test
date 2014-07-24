* Test to show how latest Bokeh release doesn't work as advertised

** What this repo consists of

* Sample script that starts up Flask microframework
* Sample Bokeh plotting script should draw a circle
* The circle plot should be visible in the `plot.html` template
* The `plot.html` template is rendered with a request to the root dir ('/')

** How to run

* Load everything from REQUIREMENTS file with

    pip install -r REQUIREMENTS.txt

* From the command line:

    python run.py


** What should happen

* Dynamically created JS files written out to
```
static-flask-bokeh/js/tmp/
```
* Dynamically created Bokeh plots displayed at root page
```
http://127.0.0.1:5000/
```
** What does happen

* Dynamically created JS files written out to
```
static-flask-bokeh/js/tmp/
```
* Flask server outputs 404 errors for the TMP js files

```python
$ python run.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
 Path: static-flask-bokeh/js/tmp/70464b2b-5ecf-46f0-ae12-606c289da4c9.js
 Wrote 70464b2b-5ecf-46f0-ae12-606c289da4c9.js
 127.0.0.1 - - [24/Jul/2014 09:19:08] "GET / HTTP/1.1" 200 -
 127.0.0.1 - - [24/Jul/2014 09:19:08] "GET /static-flask-bokeh/js/tmp/70464b2b-5ecf-46f0-ae12-606c289da4c9.js HTTP/1.1" 404 -
```

** What do I think the problem is?

Either Flask or Bokeh does not look in the specified TMP directory.
Looks like a `root_url` or `root_dir` problem in the Bokeh `Resources()` class? 

# Test to show how latest Bokeh release doesn't work as advertised

## What this repo consists of

* Sample script that starts up Flask microframework
* Sample Bokeh plotting script should draw a circle
* The circle plot should be visible in the `plot.html` template
* The `plot.html` template is rendered with a request to the root dir ('/')

## How to run

* Load everything from REQUIREMENTS file with
```
pip install -r REQUIREMENTS.txt
```
* From the command line:
```
python run.py
```

## What should happen

* Dynamically created JS files written out to
```
static-flask-bokeh/js/tmp/
```
* Dynamically created Bokeh plots displayed at root page
```
http://127.0.0.1:5000/
```

## What does happen

* Dynamically created JS files written out to
```
static-flask-bokeh/js/tmp/
```
* Here is the directory structure after running the server and hitting it a few times:
```
$ tree static-flask-bokeh/
static-flask-bokeh/
├── css
│   ├── bokeh-0.4.min.css
│   └── bokeh.min.css.old
└── js
    ├── bokeh-0.4.min.js
    ├── bokeh.min.js.old
    └── tmp
        ├── 167a9c91-9d9d-466c-ace7-b6f4f9c5834e.js
        ├── 3ea19b8f-3229-43b2-bfb8-9a7caf9ea5be.js
        ├── 48aaeb6c-59fb-4ff8-a67a-3c8cff7875ee.js
        ├── 70464b2b-5ecf-46f0-ae12-606c289da4c9.js
        ├── 8d276a60-4e85-42b0-a776-18e8d963fad6.js
        └── 9cf0cb07-ce48-417e-b278-e9a740a6cdd7.js
3 directories, 10 files
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

* Looking at the HTML rendered:

```html
<!doctype html>
<html>
  <head>
    <title>
  Circle Plot Test
    </title>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.js"></script>
    <script type="text/javascript" src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
  <style type="text/css">
  .bokeh_canvas_wrapper {
    width: 10em !important;
  }
  .bokeh .btn-group {
    margin-left: 9em;
  }
  </style>

  </head>
  <body>
  <div class="container-fluid">
    <div class="page-header">
      <h1>Circle Plot</h1>
    </div>
    <div id="3ea19b8f-3229-43b2-bfb8-9a7caf9ea5be" class="col-md-10 col-md-offset-1">
      <script
    src="static-flask-bokeh/js/tmp/3ea19b8f-3229-43b2-bfb8-9a7caf9ea5be.js"
    id="76f4b1da-d388-4603-9943-fdeba1476f57"
    async="true"
    data-bokeh-data="static"
    data-bokeh-modelid="3ea19b8f-3229-43b2-bfb8-9a7caf9ea5be"
    data-bokeh-modeltype="Plot"
></script>
    </div>
  </div>
  </body>
</html>
```

Look at the `<script src="">` path. It is a relative link. If I click
on that link I see a 404 error. That shouldn't be.

## What do I think the problem is?

Either Flask or Bokeh does not look in the specified TMP directory.
Looks like a `root_url` or `root_dir` problem in the Bokeh `Resources()` class? 

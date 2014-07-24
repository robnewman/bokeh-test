# Plotting
from bokeh.embed import autoload_static
from bokeh.resources import Resources
from bokeh.plotting import *

def circle_plot():
    """
    Pure plotting
    """
    hold()
    figure(title="Circle plot",
           x_axis_type="datetime",
           tools="pan, wheel_zoom, box_zoom, reset, previewsave",
           width=1000

    )
    circle([1,2], [3,4])
    hold()
    return curplot()

def simple_plot(plot, tmp_dir):
    js_static_js = "static-flask-bokeh/js/"
    js_static_css = "static-flask-bokeh/css/"
    js_filename = plot._id + ".js"
    js_path = tmp_dir + js_filename

    res = Resources()
    res.mode = "server"
    res.js_files = [js_static_js + "bokeh.min.js"]
    res.css_files = [js_static_css + "bokeh.min.css"]

    js, tag = autoload_static(plot,
                              res,
                              js_path)

    with open(js_path, "w") as f:
        f.write(js)
    print("Path: %s" % js_path)
    print("Wrote %s" % js_filename)
    return tag, plot._id

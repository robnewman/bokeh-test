# Plotting
from bokeh.embed import autoload_static
from bokeh.resources import Resources, CDN
from bokeh.plotting import *
# from bokeh.plotting import (hold, scatter, figure, quad, line, xgrid, ygrid,
#                             legend, curplot, patches)

# Math stuff
import numpy as np
import pandas as pd

from time import strptime, mktime
import datetime

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


def build_plot(plot, tmp_dir):
    """
    Use autoload_static overrides from
    https://github.com/damianavila/bokeh/commit/d1fdb5169e46088d529025497ae3a8a134f7cf69
    """
    js_static_js = "static-flask-bokeh/js/"
    js_static_css = "static-flask-bokeh/css/"
    js_filename = plot._id + ".js"
    js_path = tmp_dir + js_filename

    res = Resources("server")
    res.js_files = [js_static_js + "bokeh.min.js"]
    res.css_files = [js_static_css + "bokeh.min.css"]

    js, tag = autoload_static(plot,
                              res,
                              js_path)

    with open(js_path, "w") as f:
        f.write(js)
    print("Wrote %s" % js_filename)

    return tag, plot._id

def line_plot(values, title, index, plot_width, plot_height):
    """
    Pure plotting
    """

    colors = [ ('#990000', '#FF8000'),
               ('#FF0000', '#8000FF'),
               ('#00CC00', '#CCCC00'),
               ('#6600CC', '#00FFFF')
             ]

    hold()

    figure(title="Plot from host %s" % title,
           x_axis_type="datetime",
           tools="pan, wheel_zoom, box_zoom, reset, previewsave",
           width=1000
    )

    scatter(values['times'],
            values['dmcpass'],
            fill_color=None,
            line_color=colors[index][0],
            plot_width=plot_width,
            plot_height=plot_height
    )
    line(values['times'],
         values['dmcpass'],
         fill_color=None,
         line_color=colors[index][0],
         legend='dmcpass',
         line_width=2,
         line_dash=[4,4],
         plot_width=plot_width,
         plot_height=plot_height
    )

    hold()

    scatter(values['times'],
            values['adc1pass'],
            fill_color=None,
            line_color=colors[index][1],
            plot_width=plot_width,
            plot_height=plot_height
    )
    line(values['times'],
         values['adc1pass'],
         fill_color=None,
         line_color=colors[index][1],
         legend='adc1pass',
         line_width=2,
         line_dash=[4,4],
         plot_width=plot_width,
         plot_height=plot_height
    )

    return curplot()


def brewer():
    """
    Example plot ripped from github
    """
    from collections import OrderedDict
    from bokeh.palettes import brewer

    N = 20
    categories = ['y' + str(x) for x in range(10)]
    data = {}
    data['x'] = np.arange(N)
    for cat in categories:
        data[cat] = np.random.randint(10, 100, size=N)

    df = pd.DataFrame(data)
    df = df.set_index(['x'])

    def stacked(df, categories):
        areas = OrderedDict()
        last = np.zeros(len(df[categories[0]]))
        for cat in categories:
            next = last + df[cat]
            areas[cat] = np.hstack((last[::-1], next))
            last = next
        return areas

    figure(title="Brewer showcase.",
           tools="pan, wheel_zoom, box_zoom, reset, previewsave")

    areas = stacked(df, categories)

    colors = brewer["Spectral"][len(areas)]

    x2 = np.hstack((data['x'][::-1], data['x']))
    patches([x2 for a in areas], list(areas.values()), color=colors, alpha=0.8, line_color=None)

    return curplot()

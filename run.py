#!/usr/bin/env python

# FLask
from flask import Flask, render_template

# Plotting
from plots import circle_plot, simple_plot

app = Flask(__name__)
app.config.from_object('conf.configmodule.Config')

@app.route('/')
def render_plot():
    tag1, id1 = simple_plot(circle_plot(),app.config['TMP_DIR'])
    return render_template('plot.html',
                           tag1=tag1, id1=id1,
           )

if __name__ == '__main__':
    app.run()

#!/usr/bin/env python3

from flask import Flask, render_template
from flask_weasyprint import HTML, CSS, render_pdf
app = Flask(__name__)


@app.route("/")
def template_main():
    return render_template('main.html', temps=temp_table(), pa=pa_table())


@app.route("/test.pdf")
def pdf_main():

    css=CSS(string='@page { size: 450mm 620mm; margin: 0.5cm; }')
    a3css = CSS(string='@page { size: A3; margin: 0.5cm; }')
    html = render_template('main.html', temps=temp_table(), pa=pa_table())
    return render_pdf(HTML(string=html), stylesheets=[css])

def temp_table():
    temps = []
    for i in range(0,24):
        temp = i+14
        if temp < 24:
            temps.append(temp)
        else:
            temps.append(temp-24)
    return temps

def pa_table():
    pa = [30, 24, 20, 15, 10, 5, 0]
    return pa

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
#!flask/bin/python
# -- coding: utf-8 --

from flask import render_template
from flask import Flask
import os
import ctypes
app = Flask(__name__)


@app.route('/')
def hello():

    return 'python master分支,修改了代码'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

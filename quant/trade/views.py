#-*- coding:utf-8 -*-

import json
import time
import datetime
from flask import redirect, url_for, session, Blueprint, url_for, render_template, request, abort, flash, session, redirect, make_response

mod = Blueprint('quant', __name__, url_prefix='/trade')

@mod.route('/')
def loading():
    return 'Hello World!'



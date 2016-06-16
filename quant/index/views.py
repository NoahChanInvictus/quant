#-*- coding:utf-8 -*-

import json
import time
import datetime
#from user_portrait.time_utils import ts2datetime, ts2date
from flask import redirect, url_for, session, Blueprint, url_for, render_template, request, abort, flash, session, redirect, make_response
#from flask.ext.login import login_required

mod = Blueprint('quant', __name__, url_prefix='/')

@mod.route('/')
#@login_required
def loading():
    return 'Hello World!'



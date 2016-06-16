# -*- coding: utf-8 -*-

from flask import Flask
from elasticsearch import Elasticsearch
from flask_debugtoolbar import DebugToolbarExtension
from quant.index.views import mod as indexModule

def create_app():
    app = Flask(__name__)

    register_blueprints(app)
    register_extensions(app)
    register_jinja_funcs(app)

    # Create modules
    # the debug toolbar is only enabled in debug mode
    app.config['DEBUG'] = True

    app.config['ADMINS'] = frozenset(['youremail@yourdomain.com'])
    app.config['SECRET_KEY'] = 'SecretKeyForSessionSigning'
    
    app.config['DATABASE_CONNECT_OPTIONS'] = {}

    app.config['THREADS_PER_PAGE'] = 8

    app.config['CSRF_ENABLED'] = True
    app.config['CSRF_SESSION_KEY'] = 'somethingimpossibletoguess'

    # Enable the toolbar?
    app.config['DEBUG_TB_ENABLED'] = app.debug
    # Should intercept redirects?
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
    # Enable the profiler on all requests, default to false
    app.config['DEBUG_TB_PROFILER_ENABLED'] = True
    # Enable the template editor, default to false
    app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
    
    # debug toolbar
    # toolbar = DebugToolbarExtension(app)
    
    return app
   

def register_blueprints(app):
    app.register_blueprint(indexModule)
    return

def register_extensions(app):

    #login_manager.init_app(app);
    #login_manager.login_view = 'login.user'
    return

def register_jinja_funcs(app):
    return

#!/usr/bin/env python
# -*- coding: utf-8 -*-


from framework import bottle
import views


#urls para enrrutamiento
urls = [
    ('/', ['GET'], views.index),
    ('/',['POST'], views.do_index),
]


def routing(app):
    for url in urls:
        app.route(url[0], url[1], url[2])



app = bottle.Bottle()
routing(app)

# launch the App
bottle.debug(mode=True)
bottle.run(app=app, server="gae")







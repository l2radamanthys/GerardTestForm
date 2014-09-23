#!/usr/bin/env python
# -*- coding: utf-8 -*-


from framework.bottle import template, request



def index():
    return template('form.html')




def do_index():
    data = {}
    data['name'] = request.forms.get('name')
    data['phone'] = request.forms.get('phone')
    return template('saludo.html', data)
    

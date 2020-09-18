import logging

from flask import render_template, request, redirect, url_for

from . import control_center
from .forms import TapEntryForm


@control_center.route('/', methods=['POST', 'GET'])
def control_dashboard():
    """Control center dashboard view"""
    return render_template('dashboard.html')


@control_center.route('/new-entry', methods=['POST', 'GET'])
def new_entry():
    """Creates new entry"""
    form = TapEntryForm()
    if request.method == 'POST' and form.validate():
        return redirect(url_for('control_center.new_entry'))
    return render_template('new_entry.html',
                           title='Control Center',
                           form=form,
                           )

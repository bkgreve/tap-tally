import logging

from flask import render_template, request, redirect, url_for, flash

from . import control_center
from .forms import TapEntryForm, SelectEntries
from ..models.tap_entry import TapEntry
from .. import db


@control_center.route('/', methods=['GET'])
def control_dashboard():
    """Control center dashboard view"""
    visible_entries = (db.session.query(TapEntry)
                       .filter(TapEntry.visible == True)
                       .all()
                       )
    hidden_entries = (TapEntry.query.filter(TapEntry.visible == False))

    return render_template('dashboard.html',
                           visible_entries=visible_entries,
                           hidden_entries=hidden_entries,
                           )


@control_center.route('/new-entry', methods=['POST', 'GET'])
def new_entry():
    """Creates new entry"""
    form = TapEntryForm()
    entry = TapEntry()
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        db.session.add(entry)
        db.session.commit()
        flash(f"{form.name.data} added.")
        return redirect(url_for('control_center.new_entry'))
    return render_template('entry.html',
                           title='Add New Entry',
                           form=form,
                           )


@control_center.route('/edit-entry/<entry_id>', methods=['POST', 'GET'])
def edit_entry(entry_id):
    if not entry_id:
        return redirect(url_for('control_center.new_entry'))
    entry = db.session.query(TapEntry).get(entry_id)
    form = TapEntryForm(obj=entry)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('control_center.control_dashboard'))
    return render_template('entry.html',
                           title='View/Edit Entry',
                           form=form,
                           )

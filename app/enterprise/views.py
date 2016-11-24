# -*- coding: utf-8 -*-
from flask import json
from flask import render_template, session, redirect, url_for
from flask import request
from flask_login import current_app, current_user, login_required

from app.models import Permission
from . import enterprise
from ..datasource.query_enterprise import QueryEnterprise


@enterprise.route('/', methods=['GET', 'POST'])
def index():
    return render_template('enterprise/index.html')


@enterprise.route('/search', methods=['GET'])
def search():
    key = request.args.get('key')
    index = request.args.get('index')
    page_size = request.args.get('page_size')
    if not index:
        result = QueryEnterprise.company_list(query=key, page_size=page_size)
        return render_template('enterprise/search.html', data=json.loads(result))
    else:
        result = QueryEnterprise.query(key=key, index=index, page_size=page_size)
        return render_template('enterprise/search.html', data=json.loads(request))


@enterprise.route('/result')
def result():
    return render_template('enterprise/result.html')


@enterprise.route('/user/<username>')
def user(username):
    pass

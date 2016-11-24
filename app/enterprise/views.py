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
    # index = request.args.get('index')
    page_size = request.args.get('page_size')
    result = QueryEnterprise.company_list(query=key, page_size=page_size)
    return render_template('enterprise/search.html', data=json.loads(result))


@enterprise.route('/result', methods=['GET'])
def result():
    enterprise_name = request.args.get('company')
    result = QueryEnterprise.query_basic(enterprise_name=enterprise_name)
    return render_template('enterprise/result.html', data=json.loads(result))


@enterprise.route('/result/annualReport', methods=['GET'])
def annual_report():
    enterprise_name = request.args.get('company')


@enterprise.route('/result/basicInfo', methods=['GET'])
def basic_info():
    enterprise_name = request.args.get('company')
    result = QueryEnterprise.query_basic(enterprise_name=enterprise_name)
    return render_template('enterprise/_baseInfo.html', data=json.loads(result))

@enterprise.route('/user/<username>')
def user(username):
    pass

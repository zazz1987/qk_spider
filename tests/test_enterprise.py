# -*- coding: utf-8 -*-
import pytest as pytest
from flask import url_for
from mock import mock

from app import create_app, db
from app.datasource.query_enterprise import QueryEnterprise
from app.models import Role


class TestEnterprise():

    @pytest.fixture(scope='class')
    def setup(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def test_search(self, setup):
        result = self.client.get(url_for('enterprise.search'))
        assert result

    def test_query_qualifiction(self):
        result = QueryEnterprise.query_qualifiction(company=u'小米科技有限责任公司')
        print(result)


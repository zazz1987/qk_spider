# -*- coding: utf-8 -*-
import pytest as pytest
from flask import url_for
from mock import mock

from app import create_app, db
from app.models import Role


class TestEnterprist():

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

